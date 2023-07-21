import re
from typing import Dict
from warnings import warn

from deprecated import deprecated
from gql import Client
from gql.transport.exceptions import TransportServerError
from gql.transport.requests import RequestsHTTPTransport
from gql.transport.websockets import WebsocketsTransport

from specklepy.api import resources
from specklepy.api.credentials import Account, get_account_from_token
from specklepy.api.resources import (
    active_user,
    branch,
    commit,
    object,
    other_user,
    server,
    stream,
    subscriptions,
)
from specklepy.logging import metrics
from specklepy.logging.exceptions import SpeckleException, SpeckleWarning

from specklepy.core.api.client import SpeckleClient as CoreSpeckleClient


class SpeckleClient(CoreSpeckleClient):
    """
    The `SpeckleClient` is your entry point for interacting with
    your Speckle Server's GraphQL API.
    You'll need to have access to a server to use it,
    or you can use our public server `speckle.xyz`.

    To authenticate the client, you'll need to have downloaded
    the [Speckle Manager](https://speckle.guide/#speckle-manager)
    and added your account.

    ```py
    from specklepy.api.client import SpeckleClient
    from specklepy.api.credentials import get_default_account

    # initialise the client
    client = SpeckleClient(host="speckle.xyz") # or whatever your host is
    # client = SpeckleClient(host="localhost:3000", use_ssl=False) or use local server

    # authenticate the client with an account (account has been added in Speckle Manager)
    account = get_default_account()
    client.authenticate_with_account(account)

    # create a new stream. this returns the stream id
    new_stream_id = client.stream.create(name="a shiny new stream")

    # use that stream id to get the stream from the server
    new_stream = client.stream.get(id=new_stream_id)
    ```
    """

    DEFAULT_HOST = "speckle.xyz"
    USE_SSL = True

    def __init__(self, host: str = DEFAULT_HOST, use_ssl: bool = USE_SSL) -> None:
        super().__init__(
            host=host,
            use_ssl=use_ssl,
        )
        self.account = Account()

    @deprecated(
        version="2.6.0",
        reason=(
            "Renamed: please use `authenticate_with_account` or"
            " `authenticate_with_token` instead."
        ),
    )
    def authenticate(self, token: str) -> None:
        """Authenticate the client using a personal access token
        The token is saved in the client object and a synchronous GraphQL
        entrypoint is created

        Arguments:
            token {str} -- an api token
        """
        metrics.track(metrics.SDK, self.account, {"name": "Client Authenticate_deprecated"})
        return super().authenticate(token)

    def authenticate_with_token(self, token: str) -> None:
        """
        Authenticate the client using a personal access token.
        The token is saved in the client object and a synchronous GraphQL
        entrypoint is created

        Arguments:
            token {str} -- an api token
        """
        metrics.track(metrics.SDK, self.account, {"name": "Client Authenticate With Token"})
        return super().authenticate_with_token(token)

    def authenticate_with_account(self, account: Account) -> None:
        """Authenticate the client using an Account object
        The account is saved in the client object and a synchronous GraphQL
        entrypoint is created

        Arguments:
            account {Account} -- the account object which can be found with
            `get_default_account` or `get_local_accounts`
        """
        metrics.track(metrics.SDK, self.account, {"name": "Client Authenticate With Account"})
        return super().authenticate_with_account(account)
