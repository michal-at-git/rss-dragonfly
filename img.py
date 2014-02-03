#!/usr/bin/python
# coding: utf-8
error = "data:image/png;base64,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"