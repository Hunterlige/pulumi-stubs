import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetNotificationChannelResult",
    "AwaitableGetNotificationChannelResult",
    "get_notification_channel",
    "get_notification_channel_output",
]

@pulumi.output_type
class GetNotificationChannelResult:
    def __init__(__self__, filters=..., id=..., region=..., sns=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def filters(
        self,
    ) -> Optional[Sequence[outputs.GetNotificationChannelFilterResult]]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def sns(self) -> Optional[Sequence[outputs.GetNotificationChannelSnResult]]: ...

class AwaitableGetNotificationChannelResult(GetNotificationChannelResult):
    def __await__(self): ...

def get_notification_channel(
    filters: Optional[
        Sequence[
            Union[
                GetNotificationChannelFilterArgs, GetNotificationChannelFilterArgsDict
            ]
        ]
    ] = ...,
    id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    sns: Optional[
        Sequence[Union[GetNotificationChannelSnArgs, GetNotificationChannelSnArgsDict]]
    ] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetNotificationChannelResult: ...
def get_notification_channel_output(
    filters: Optional[
        pulumi.Input[
            Optional[
                Sequence[
                    Union[
                        GetNotificationChannelFilterArgs,
                        GetNotificationChannelFilterArgsDict,
                    ]
                ]
            ]
        ]
    ] = ...,
    id: Optional[pulumi.Input[_builtins.str]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    sns: Optional[
        pulumi.Input[
            Optional[
                Sequence[
                    Union[
                        GetNotificationChannelSnArgs, GetNotificationChannelSnArgsDict
                    ]
                ]
            ]
        ]
    ] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetNotificationChannelResult]: ...
