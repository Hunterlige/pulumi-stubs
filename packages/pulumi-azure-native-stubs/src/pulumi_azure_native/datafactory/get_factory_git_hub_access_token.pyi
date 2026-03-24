

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetFactoryGitHubAccessTokenResult', 'AwaitableGetFactoryGitHubAccessTokenResult', 'get_factory_git_hub_access_token', 'get_factory_git_hub_access_token_output']
@pulumi.output_type
class GetFactoryGitHubAccessTokenResult:
    
    def __init__(__self__, git_hub_access_token=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gitHubAccessToken")
    def git_hub_access_token(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableGetFactoryGitHubAccessTokenResult(GetFactoryGitHubAccessTokenResult):
    def __await__(self): # -> Generator[Never, Any, GetFactoryGitHubAccessTokenResult]:
        ...
    


def get_factory_git_hub_access_token(factory_name: Optional[_builtins.str] = ..., git_hub_access_code: Optional[_builtins.str] = ..., git_hub_access_token_base_url: Optional[_builtins.str] = ..., git_hub_client_id: Optional[_builtins.str] = ..., git_hub_client_secret: Optional[Union[GitHubClientSecret, GitHubClientSecretDict]] = ..., resource_group_name: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetFactoryGitHubAccessTokenResult:
    
    ...

def get_factory_git_hub_access_token_output(factory_name: Optional[pulumi.Input[_builtins.str]] = ..., git_hub_access_code: Optional[pulumi.Input[_builtins.str]] = ..., git_hub_access_token_base_url: Optional[pulumi.Input[_builtins.str]] = ..., git_hub_client_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., git_hub_client_secret: Optional[pulumi.Input[Optional[Union[GitHubClientSecret, GitHubClientSecretDict]]]] = ..., resource_group_name: Optional[pulumi.Input[_builtins.str]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetFactoryGitHubAccessTokenResult]:
    
    ...

