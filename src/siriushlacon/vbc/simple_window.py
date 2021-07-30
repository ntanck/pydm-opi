#!/usr/bin/env python3
import logging

from pydm import Display

from siriushlacon.utils.command_runner import CommandRunner
from siriushlacon.utils.images import LNLS_PIXMAP
from siriushlacon.vbc.confirmation_message import ConfirmationMessageDialog
from siriushlacon.vbc.consts import SIMPLE_WINDOW_UI
from siriushlacon.vbc.scripts import commute_valve

logger = logging.getLogger(__name__)


class DeviceMenu(Display):
    def __init__(self, parent=None, args=None, macros=None):
        super(DeviceMenu, self).__init__(
            parent=parent, args=args, macros=macros, ui_filename=SIMPLE_WINDOW_UI
        )
        self.lnlsLabel.setPixmap(LNLS_PIXMAP)
        self.lnlsLabel.setFixedSize(LNLS_PIXMAP.size())

        self.prefix: str = macros["IOC"]

        self.CommuteValve1Command = CommandRunner(
            command=lambda: commute_valve(prefix=self.prefix, valve=1, confirmed=True),
            name="CommuteValve1_True",
        )

        self.CommuteValve2Command = CommandRunner(
            command=lambda: commute_valve(prefix=self.prefix, valve=2, confirmed=True),
            name="CommuteValve2_True",
        )

        self.ChkBoxPreVacValve.clicked.connect(
            lambda *_args, **_kwargs: self.CommuteValve1Command.execute_command()
        )
        self.ChkGateValve.clicked.connect(
            lambda *_args, **_kwargs: self.CommuteValve2Command.execute_command()
        )
        self.ChkTurboVentingValve.clicked.connect(self.show_confirmation_message)

    def show_confirmation_message(self, *_args, **_kwargs):
        dialog = ConfirmationMessageDialog(
            parent=self, prefix=self.prefix, relay_number=5, macros=self.macros()
        )
        dialog.show()
