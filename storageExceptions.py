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


class VolumeAlreadyExported(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"[{type(self).__name__}] {self.message}"


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


class VolumeNotExportable(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"[{type(self).__name__}] {self.message}"
    

class VolumeNotAllocable(Exception):
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
    

class VolumeAlredyLocked(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"[{type(self).__name__}] {self.message}"
    
class VolumeCannotBeDeleted(Exception):
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
    

class CloudInitDownloadfailed(Exception):
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