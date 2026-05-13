import os
import sys
import importlib
from qgis.PyQt.QtWidgets import QMessageBox


def check():
    # Check if required packages are installed
    missing_packages = []

    try:
        from PIL import ImageFont
        ImageFont.truetype("arial.ttf", 16)
    except:
        package = 'pillow'
        missing_packages.append(package)

    if missing_packages:
        message = "The following Python package is required update to use the plugin QCopycanvas:\n\n"
        message += "\n".join(missing_packages)
        message += "\n\nWould you like to install them now?"

        reply = QMessageBox.question(None, 'Missing Dependencies', message,
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                     QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.No:
            return

        try:
            import subprocess
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', '--force-reinstall',
                                   '--no-cache-dir', 'pillow'])
        finally:
            QMessageBox.information(None, 'Install successfully.', 'Please restart QGIS to use QCopycanvas plugin.')
