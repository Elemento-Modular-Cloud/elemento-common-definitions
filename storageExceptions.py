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


class VolumeMetadataDoesNotExist(Exception):
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


class VolumeDataDoesNotExist(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"[{type(self).__name__}] {self.message}"


### EXPORT ###
class VolumeAlreadyExported(Exception):
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


### METADATA NOT VALID ###
class VolumeBusNotAllowed(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"[{type(self).__name__}] {self.message}"


class VolumeFormatNotAllowed(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"[{type(self).__name__}] {self.message}"


class VolumeCloningAlgNotAllowed(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"[{type(self).__name__}] {self.message}"


### METADATA UPDATE ###
class VolumeMetadataNotUpdatable(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"[{type(self).__name__}] {self.message}"


class VolumeImpossibleFormatMetaUpdate(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"[{type(self).__name__}] {self.message}"


class VolumeImpossibleCreatorIDMetaUpdate(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"[{type(self).__name__}] {self.message}"


class VolumeImpossibleCloudinitMetaUpdate(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"[{type(self).__name__}] {self.message}"


### RESIZE ###
class VolumeDimensionNotUpdatable(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"[{type(self).__name__}] {self.message}"


class VolumeDimensionNotShrinkable(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"[{type(self).__name__}] {self.message}"


### CREATE ###
class VolumeNotAllocable(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"[{type(self).__name__}] {self.message}"

class VolumeCannotBeCreated(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"[{type(self).__name__}] {self.message}"


class VolumeAvailablePathNotFound(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"[{type(self).__name__}] {self.message}"


class VolumeDimensionNotFound(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"[{type(self).__name__}] {self.message}"


class VolumeFormatNotFound(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"[{type(self).__name__}] {self.message}"


### LOCK ACTIONS ###
class VolumeAlredyLocked(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"[{type(self).__name__}] {self.message}"


class VolumeAlredyUnlocked(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"[{type(self).__name__}] {self.message}"


### BIN AND DELETE ###
class VolumeCannotBeDeleted(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"[{type(self).__name__}] {self.message}"


class ElementoBinNotFound(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"[{type(self).__name__}] {self.message}"


### CLOUDINIT ###
class CloudInitCreateImageDownloadfailed(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"[{type(self).__name__}] {self.message}"


class CloudInitMetadataUploadFailed(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"[{type(self).__name__}] {self.message}"


class CloudInitMetadataFileNotFound(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"[{type(self).__name__}] {self.message}"


class CloudInitIsoCreationFailed(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"[{type(self).__name__}] {self.message}"


class ClouInitIsoNotFound(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"[{type(self).__name__}] {self.message}"


class CloudInitMetafilesNumberExceeded(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"[{type(self).__name__}] {self.message}"


class CloudInitExpectedFilesTrackerNotFound(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"[{type(self).__name__}] {self.message}"


# overlay
class UnsupportedFormat(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"[{type(self).__name__}] {self.message}"