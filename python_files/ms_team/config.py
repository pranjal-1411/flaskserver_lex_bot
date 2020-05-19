#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "6da29de7-e78b-4734-9486-5f78efb2c0be")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword","1BuAOGXv5~_7Mx-f~3X_4849EW_1Ubt021")
