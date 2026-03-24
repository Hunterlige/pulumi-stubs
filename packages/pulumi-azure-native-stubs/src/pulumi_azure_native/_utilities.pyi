

import typing
import pulumi
import pulumi.runtime

C = typing.TypeVar("C", bound=typing.Callable)
def get_env(*args): # -> str | None:
    ...

def get_env_bool(*args): # -> bool | None:
    ...

def get_env_int(*args): # -> int | None:
    ...

def get_env_float(*args): # -> float | None:
    ...

_version = _get_semver_version()
_version_str = ...
def get_resource_opts_defaults() -> pulumi.ResourceOptions:
    ...

def get_invoke_opts_defaults() -> pulumi.InvokeOptions:
    ...

def get_resource_args_opts(resource_args_type, resource_options_type, *args, **kwargs): # -> tuple[Any | None, Any | None]:
    
    ...

def lazy_import(fullname): # -> ModuleType | Any:
    ...

class Package(pulumi.runtime.ResourcePackage):
    def __init__(self, pkg_info) -> None:
        ...
    
    def version(self): # -> VersionInfo:
        ...
    
    def construct_provider(self, name: str, typ: str, urn: str) -> pulumi.ProviderResource:
        ...
    


class Module(pulumi.runtime.ResourceModule):
    def __init__(self, mod_info) -> None:
        ...
    
    def version(self): # -> VersionInfo:
        ...
    
    def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
        ...
    


def register(resource_modules, resource_packages): # -> None:
    ...

_F = typing.TypeVar('_F', bound=typing.Callable[..., typing.Any])
def lift_output_func(func: typing.Any) -> typing.Callable[[_F], _F]:
    
    ...

def call_plain(tok: str, props: pulumi.Inputs, res: typing.Optional[pulumi.Resource] = ..., typ: typing.Optional[type] = ...) -> typing.Any:
    
    ...

def deprecated(message: str) -> typing.Callable[[C], C]:
    
    ...

def get_plugin_download_url(): # -> None:
    ...

def get_version(): # -> str:
    ...

