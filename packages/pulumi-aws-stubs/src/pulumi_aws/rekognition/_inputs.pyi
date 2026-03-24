

import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CollectionTimeoutsArgs', 'CollectionTimeoutsArgsDict', 'ProjectTimeoutsArgs', 'ProjectTimeoutsArgsDict', 'StreamProcessorDataSharingPreferenceArgs', 'StreamProcessorDataSharingPreferenceArgsDict', 'StreamProcessorInputArgs', 'StreamProcessorInputArgsDict', 'StreamProcessorInputKinesisVideoStreamArgs', 'StreamProcessorInputKinesisVideoStreamArgsDict', 'StreamProcessorNotificationChannelArgs', 'StreamProcessorNotificationChannelArgsDict', 'StreamProcessorOutputArgs', 'StreamProcessorOutputArgsDict', 'StreamProcessorOutputKinesisDataStreamArgs', 'StreamProcessorOutputKinesisDataStreamArgsDict', 'StreamProcessorOutputS3DestinationArgs', 'StreamProcessorOutputS3DestinationArgsDict', 'StreamProcessorRegionsOfInterestArgs', 'StreamProcessorRegionsOfInterestArgsDict', 'StreamProcessorRegionsOfInterestBoundingBoxArgs', ..., 'StreamProcessorRegionsOfInterestPolygonArgs', 'StreamProcessorRegionsOfInterestPolygonArgsDict', 'StreamProcessorSettingsArgs', 'StreamProcessorSettingsArgsDict', 'StreamProcessorSettingsConnectedHomeArgs', 'StreamProcessorSettingsConnectedHomeArgsDict', 'StreamProcessorSettingsFaceSearchArgs', 'StreamProcessorSettingsFaceSearchArgsDict', 'StreamProcessorTimeoutsArgs', 'StreamProcessorTimeoutsArgsDict']
class CollectionTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CollectionTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ProjectTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ProjectTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., delete: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class StreamProcessorDataSharingPreferenceArgsDict(TypedDict):
    opt_in: pulumi.Input[_builtins.bool]


@pulumi.input_type
class StreamProcessorDataSharingPreferenceArgs:
    def __init__(__self__, *, opt_in: pulumi.Input[_builtins.bool]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="optIn")
    def opt_in(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @opt_in.setter
    def opt_in(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    


class StreamProcessorInputArgsDict(TypedDict):
    kinesis_video_stream: pulumi.Input[StreamProcessorInputKinesisVideoStreamArgsDict]


@pulumi.input_type
class StreamProcessorInputArgs:
    def __init__(__self__, *, kinesis_video_stream: pulumi.Input[StreamProcessorInputKinesisVideoStreamArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kinesisVideoStream")
    def kinesis_video_stream(self) -> pulumi.Input[StreamProcessorInputKinesisVideoStreamArgs]:
        
        ...
    
    @kinesis_video_stream.setter
    def kinesis_video_stream(self, value: pulumi.Input[StreamProcessorInputKinesisVideoStreamArgs]): # -> None:
        ...
    


class StreamProcessorInputKinesisVideoStreamArgsDict(TypedDict):
    arn: pulumi.Input[_builtins.str]


@pulumi.input_type
class StreamProcessorInputKinesisVideoStreamArgs:
    def __init__(__self__, *, arn: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @arn.setter
    def arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class StreamProcessorNotificationChannelArgsDict(TypedDict):
    sns_topic_arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class StreamProcessorNotificationChannelArgs:
    def __init__(__self__, *, sns_topic_arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="snsTopicArn")
    def sns_topic_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @sns_topic_arn.setter
    def sns_topic_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class StreamProcessorOutputArgsDict(TypedDict):
    kinesis_data_stream: NotRequired[pulumi.Input[StreamProcessorOutputKinesisDataStreamArgsDict]]
    s3_destination: NotRequired[pulumi.Input[StreamProcessorOutputS3DestinationArgsDict]]


@pulumi.input_type
class StreamProcessorOutputArgs:
    def __init__(__self__, *, kinesis_data_stream: Optional[pulumi.Input[StreamProcessorOutputKinesisDataStreamArgs]] = ..., s3_destination: Optional[pulumi.Input[StreamProcessorOutputS3DestinationArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kinesisDataStream")
    def kinesis_data_stream(self) -> Optional[pulumi.Input[StreamProcessorOutputKinesisDataStreamArgs]]:
        
        ...
    
    @kinesis_data_stream.setter
    def kinesis_data_stream(self, value: Optional[pulumi.Input[StreamProcessorOutputKinesisDataStreamArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="s3Destination")
    def s3_destination(self) -> Optional[pulumi.Input[StreamProcessorOutputS3DestinationArgs]]:
        
        ...
    
    @s3_destination.setter
    def s3_destination(self, value: Optional[pulumi.Input[StreamProcessorOutputS3DestinationArgs]]): # -> None:
        ...
    


class StreamProcessorOutputKinesisDataStreamArgsDict(TypedDict):
    arn: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class StreamProcessorOutputKinesisDataStreamArgs:
    def __init__(__self__, *, arn: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class StreamProcessorOutputS3DestinationArgsDict(TypedDict):
    bucket: NotRequired[pulumi.Input[_builtins.str]]
    key_prefix: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class StreamProcessorOutputS3DestinationArgs:
    def __init__(__self__, *, bucket: Optional[pulumi.Input[_builtins.str]] = ..., key_prefix: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyPrefix")
    def key_prefix(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key_prefix.setter
    def key_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class StreamProcessorRegionsOfInterestArgsDict(TypedDict):
    bounding_box: NotRequired[pulumi.Input[StreamProcessorRegionsOfInterestBoundingBoxArgsDict]]
    polygons: NotRequired[pulumi.Input[Sequence[pulumi.Input[StreamProcessorRegionsOfInterestPolygonArgsDict]]]]


@pulumi.input_type
class StreamProcessorRegionsOfInterestArgs:
    def __init__(__self__, *, bounding_box: Optional[pulumi.Input[StreamProcessorRegionsOfInterestBoundingBoxArgs]] = ..., polygons: Optional[pulumi.Input[Sequence[pulumi.Input[StreamProcessorRegionsOfInterestPolygonArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="boundingBox")
    def bounding_box(self) -> Optional[pulumi.Input[StreamProcessorRegionsOfInterestBoundingBoxArgs]]:
        
        ...
    
    @bounding_box.setter
    def bounding_box(self, value: Optional[pulumi.Input[StreamProcessorRegionsOfInterestBoundingBoxArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def polygons(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[StreamProcessorRegionsOfInterestPolygonArgs]]]]:
        
        ...
    
    @polygons.setter
    def polygons(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[StreamProcessorRegionsOfInterestPolygonArgs]]]]): # -> None:
        ...
    


class StreamProcessorRegionsOfInterestBoundingBoxArgsDict(TypedDict):
    height: NotRequired[pulumi.Input[_builtins.float]]
    left: NotRequired[pulumi.Input[_builtins.float]]
    top: NotRequired[pulumi.Input[_builtins.float]]
    width: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class StreamProcessorRegionsOfInterestBoundingBoxArgs:
    def __init__(__self__, *, height: Optional[pulumi.Input[_builtins.float]] = ..., left: Optional[pulumi.Input[_builtins.float]] = ..., top: Optional[pulumi.Input[_builtins.float]] = ..., width: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def height(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @height.setter
    def height(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def left(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @left.setter
    def left(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def top(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @top.setter
    def top(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def width(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @width.setter
    def width(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class StreamProcessorRegionsOfInterestPolygonArgsDict(TypedDict):
    x: NotRequired[pulumi.Input[_builtins.float]]
    y: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class StreamProcessorRegionsOfInterestPolygonArgs:
    def __init__(__self__, *, x: Optional[pulumi.Input[_builtins.float]] = ..., y: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def x(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @x.setter
    def x(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def y(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @y.setter
    def y(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class StreamProcessorSettingsArgsDict(TypedDict):
    connected_home: NotRequired[pulumi.Input[StreamProcessorSettingsConnectedHomeArgsDict]]
    face_search: NotRequired[pulumi.Input[StreamProcessorSettingsFaceSearchArgsDict]]


@pulumi.input_type
class StreamProcessorSettingsArgs:
    def __init__(__self__, *, connected_home: Optional[pulumi.Input[StreamProcessorSettingsConnectedHomeArgs]] = ..., face_search: Optional[pulumi.Input[StreamProcessorSettingsFaceSearchArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectedHome")
    def connected_home(self) -> Optional[pulumi.Input[StreamProcessorSettingsConnectedHomeArgs]]:
        
        ...
    
    @connected_home.setter
    def connected_home(self, value: Optional[pulumi.Input[StreamProcessorSettingsConnectedHomeArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="faceSearch")
    def face_search(self) -> Optional[pulumi.Input[StreamProcessorSettingsFaceSearchArgs]]:
        
        ...
    
    @face_search.setter
    def face_search(self, value: Optional[pulumi.Input[StreamProcessorSettingsFaceSearchArgs]]): # -> None:
        ...
    


class StreamProcessorSettingsConnectedHomeArgsDict(TypedDict):
    labels: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    min_confidence: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class StreamProcessorSettingsConnectedHomeArgs:
    def __init__(__self__, *, labels: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., min_confidence: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="minConfidence")
    def min_confidence(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @min_confidence.setter
    def min_confidence(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class StreamProcessorSettingsFaceSearchArgsDict(TypedDict):
    collection_id: pulumi.Input[_builtins.str]
    face_match_threshold: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class StreamProcessorSettingsFaceSearchArgs:
    def __init__(__self__, *, collection_id: pulumi.Input[_builtins.str], face_match_threshold: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="collectionId")
    def collection_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @collection_id.setter
    def collection_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="faceMatchThreshold")
    def face_match_threshold(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @face_match_threshold.setter
    def face_match_threshold(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class StreamProcessorTimeoutsArgsDict(TypedDict):
    create: NotRequired[pulumi.Input[_builtins.str]]
    delete: NotRequired[pulumi.Input[_builtins.str]]
    update: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class StreamProcessorTimeoutsArgs:
    def __init__(__self__, *, create: Optional[pulumi.Input[_builtins.str]] = ..., delete: Optional[pulumi.Input[_builtins.str]] = ..., update: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def create(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create.setter
    def create(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def delete(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @delete.setter
    def delete(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def update(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update.setter
    def update(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


