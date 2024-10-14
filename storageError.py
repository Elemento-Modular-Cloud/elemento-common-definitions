#!env python3


class VolumeNotFound(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"[{type(self).__name__}] {self.message}"


class VolumeMetadataNotFound(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"[{type(self).__name__}] {self.message}"


class VolumeDataNotFound(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"[{type(self).__name__}] {self.message}"


class VolumeAlreadyExported(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"[{type(self).__name__}] {self.message}"


class VolumeDimensionNotUpdatable(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"[{type(self).__name__}] {self.message}"


class VolumeNotExportable(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"[{type(self).__name__}] {self.message}"