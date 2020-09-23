from datetime import datetime, timezone


class Base:
    """Base class for 'zeitsprung-fm' package classes."""

    def __init__(self, verbose: bool = True) -> None:
        self.verbose = verbose

    def _print(self, message: str) -> None:
        if self.verbose:
            print(f'{datetime.now(timezone.utc).replace(microsecond=0).isoformat()} {message}')
