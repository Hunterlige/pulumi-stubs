import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "CollectionTimeouts",
    "ProjectTimeouts",
    "StreamProcessorDataSharingPreference",
    "StreamProcessorInput",
    "StreamProcessorInputKinesisVideoStream",
    "StreamProcessorNotificationChannel",
    "StreamProcessorOutput",
    "StreamProcessorOutputKinesisDataStream",
    "StreamProcessorOutputS3Destination",
    "StreamProcessorRegionsOfInterest",
    "StreamProcessorRegionsOfInterestBoundingBox",
    "StreamProcessorRegionsOfInterestPolygon",
    "StreamProcessorSettings",
    "StreamProcessorSettingsConnectedHome",
    "StreamProcessorSettingsFaceSearch",
    "StreamProcessorTimeouts",
]

@pulumi.output_type
class CollectionTimeouts(dict):
    def __init__(__self__, *, create: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ProjectTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StreamProcessorDataSharingPreference(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, opt_in: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter(name="optIn")
    def opt_in(self) -> _builtins.bool: ...

@pulumi.output_type
class StreamProcessorInput(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        kinesis_video_stream: outputs.StreamProcessorInputKinesisVideoStream,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kinesisVideoStream")
    def kinesis_video_stream(
        self,
    ) -> outputs.StreamProcessorInputKinesisVideoStream: ...

@pulumi.output_type
class StreamProcessorInputKinesisVideoStream(dict):
    def __init__(__self__, *, arn: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...

@pulumi.output_type
class StreamProcessorNotificationChannel(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, sns_topic_arn: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="snsTopicArn")
    def sns_topic_arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StreamProcessorOutput(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        kinesis_data_stream: Optional[
            outputs.StreamProcessorOutputKinesisDataStream
        ] = ...,
        s3_destination: Optional[outputs.StreamProcessorOutputS3Destination] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kinesisDataStream")
    def kinesis_data_stream(
        self,
    ) -> Optional[outputs.StreamProcessorOutputKinesisDataStream]: ...
    @_builtins.property
    @pulumi.getter(name="s3Destination")
    def s3_destination(
        self,
    ) -> Optional[outputs.StreamProcessorOutputS3Destination]: ...

@pulumi.output_type
class StreamProcessorOutputKinesisDataStream(dict):
    def __init__(__self__, *, arn: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StreamProcessorOutputS3Destination(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket: Optional[_builtins.str] = ...,
        key_prefix: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyPrefix")
    def key_prefix(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class StreamProcessorRegionsOfInterest(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bounding_box: Optional[
            outputs.StreamProcessorRegionsOfInterestBoundingBox
        ] = ...,
        polygons: Optional[
            Sequence[outputs.StreamProcessorRegionsOfInterestPolygon]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="boundingBox")
    def bounding_box(
        self,
    ) -> Optional[outputs.StreamProcessorRegionsOfInterestBoundingBox]: ...
    @_builtins.property
    @pulumi.getter
    def polygons(
        self,
    ) -> Optional[Sequence[outputs.StreamProcessorRegionsOfInterestPolygon]]: ...

@pulumi.output_type
class StreamProcessorRegionsOfInterestBoundingBox(dict):
    def __init__(
        __self__,
        *,
        height: Optional[_builtins.float] = ...,
        left: Optional[_builtins.float] = ...,
        top: Optional[_builtins.float] = ...,
        width: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def height(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter
    def left(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter
    def top(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter
    def width(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class StreamProcessorRegionsOfInterestPolygon(dict):
    def __init__(
        __self__,
        *,
        x: Optional[_builtins.float] = ...,
        y: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def x(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter
    def y(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class StreamProcessorSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        connected_home: Optional[outputs.StreamProcessorSettingsConnectedHome] = ...,
        face_search: Optional[outputs.StreamProcessorSettingsFaceSearch] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectedHome")
    def connected_home(
        self,
    ) -> Optional[outputs.StreamProcessorSettingsConnectedHome]: ...
    @_builtins.property
    @pulumi.getter(name="faceSearch")
    def face_search(self) -> Optional[outputs.StreamProcessorSettingsFaceSearch]: ...

@pulumi.output_type
class StreamProcessorSettingsConnectedHome(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        labels: Optional[Sequence[_builtins.str]] = ...,
        min_confidence: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="minConfidence")
    def min_confidence(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class StreamProcessorSettingsFaceSearch(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        collection_id: _builtins.str,
        face_match_threshold: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="collectionId")
    def collection_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="faceMatchThreshold")
    def face_match_threshold(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class StreamProcessorTimeouts(dict):
    def __init__(
        __self__,
        *,
        create: Optional[_builtins.str] = ...,
        delete: Optional[_builtins.str] = ...,
        update: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[_builtins.str]: ...
