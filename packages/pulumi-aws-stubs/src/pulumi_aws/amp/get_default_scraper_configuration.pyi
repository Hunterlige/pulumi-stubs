import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetDefaultScraperConfigurationResult",
    "AwaitableGetDefaultScraperConfigurationResult",
    "get_default_scraper_configuration",
    "get_default_scraper_configuration_output",
]

@pulumi.output_type
class GetDefaultScraperConfigurationResult:
    def __init__(__self__, configuration=..., id=..., region=...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def configuration(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...

class AwaitableGetDefaultScraperConfigurationResult(
    GetDefaultScraperConfigurationResult
):
    def __await__(self): ...

def get_default_scraper_configuration(
    region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...
) -> AwaitableGetDefaultScraperConfigurationResult: ...
def get_default_scraper_configuration_output(
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetDefaultScraperConfigurationResult]: ...
