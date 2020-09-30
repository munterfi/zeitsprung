from datetime import datetime, timezone


class Base:
    """Base class for 'zeitsprung-fm' package classes."""

    def __init__(self, verbose: bool = True) -> None:
        """
        Class constructor for the Base class.

        Parameters
        ----------
        verbose : bool, default True
            Print messages about the activities conducted by a class instance.

        Returns
        -------
        None

        """
        self.verbose = verbose

    def _print(self, message: str) -> None:
        if self.verbose:
            print(f'{datetime.now(timezone.utc).replace(microsecond=0).isoformat()} {message}')
