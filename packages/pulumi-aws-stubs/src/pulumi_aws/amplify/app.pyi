

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AppArgs', 'App']
@pulumi.input_type
class AppArgs:
    def __init__(__self__, *, access_token: Optional[pulumi.Input[_builtins.str]] = ..., auto_branch_creation_config: Optional[pulumi.Input[AppAutoBranchCreationConfigArgs]] = ..., auto_branch_creation_patterns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., basic_auth_credentials: Optional[pulumi.Input[_builtins.str]] = ..., build_spec: Optional[pulumi.Input[_builtins.str]] = ..., cache_config: Optional[pulumi.Input[AppCacheConfigArgs]] = ..., compute_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., custom_headers: Optional[pulumi.Input[_builtins.str]] = ..., custom_rules: Optional[pulumi.Input[Sequence[pulumi.Input[AppCustomRuleArgs]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., enable_auto_branch_creation: Optional[pulumi.Input[_builtins.bool]] = ..., enable_basic_auth: Optional[pulumi.Input[_builtins.bool]] = ..., enable_branch_auto_build: Optional[pulumi.Input[_builtins.bool]] = ..., enable_branch_auto_deletion: Optional[pulumi.Input[_builtins.bool]] = ..., environment_variables: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., iam_service_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., job_config: Optional[pulumi.Input[AppJobConfigArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., oauth_token: Optional[pulumi.Input[_builtins.str]] = ..., platform: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., repository: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @access_token.setter
    def access_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoBranchCreationConfig")
    def auto_branch_creation_config(self) -> Optional[pulumi.Input[AppAutoBranchCreationConfigArgs]]:
        
        ...
    
    @auto_branch_creation_config.setter
    def auto_branch_creation_config(self, value: Optional[pulumi.Input[AppAutoBranchCreationConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoBranchCreationPatterns")
    def auto_branch_creation_patterns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @auto_branch_creation_patterns.setter
    def auto_branch_creation_patterns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="basicAuthCredentials")
    def basic_auth_credentials(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @basic_auth_credentials.setter
    def basic_auth_credentials(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="buildSpec")
    def build_spec(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @build_spec.setter
    def build_spec(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheConfig")
    def cache_config(self) -> Optional[pulumi.Input[AppCacheConfigArgs]]:
        
        ...
    
    @cache_config.setter
    def cache_config(self, value: Optional[pulumi.Input[AppCacheConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeRoleArn")
    def compute_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @compute_role_arn.setter
    def compute_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customHeaders")
    def custom_headers(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @custom_headers.setter
    def custom_headers(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRules")
    def custom_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AppCustomRuleArgs]]]]:
        
        ...
    
    @custom_rules.setter
    def custom_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AppCustomRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAutoBranchCreation")
    def enable_auto_branch_creation(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_auto_branch_creation.setter
    def enable_auto_branch_creation(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableBasicAuth")
    def enable_basic_auth(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_basic_auth.setter
    def enable_basic_auth(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableBranchAutoBuild")
    def enable_branch_auto_build(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_branch_auto_build.setter
    def enable_branch_auto_build(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableBranchAutoDeletion")
    def enable_branch_auto_deletion(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_branch_auto_deletion.setter
    def enable_branch_auto_deletion(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @environment_variables.setter
    def environment_variables(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamServiceRoleArn")
    def iam_service_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @iam_service_role_arn.setter
    def iam_service_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobConfig")
    def job_config(self) -> Optional[pulumi.Input[AppJobConfigArgs]]:
        
        ...
    
    @job_config.setter
    def job_config(self, value: Optional[pulumi.Input[AppJobConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauthToken")
    def oauth_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @oauth_token.setter
    def oauth_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def platform(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @platform.setter
    def platform(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def repository(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @repository.setter
    def repository(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.input_type
class _AppState:
    def __init__(__self__, *, access_token: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., auto_branch_creation_config: Optional[pulumi.Input[AppAutoBranchCreationConfigArgs]] = ..., auto_branch_creation_patterns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., basic_auth_credentials: Optional[pulumi.Input[_builtins.str]] = ..., build_spec: Optional[pulumi.Input[_builtins.str]] = ..., cache_config: Optional[pulumi.Input[AppCacheConfigArgs]] = ..., compute_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., custom_headers: Optional[pulumi.Input[_builtins.str]] = ..., custom_rules: Optional[pulumi.Input[Sequence[pulumi.Input[AppCustomRuleArgs]]]] = ..., default_domain: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., enable_auto_branch_creation: Optional[pulumi.Input[_builtins.bool]] = ..., enable_basic_auth: Optional[pulumi.Input[_builtins.bool]] = ..., enable_branch_auto_build: Optional[pulumi.Input[_builtins.bool]] = ..., enable_branch_auto_deletion: Optional[pulumi.Input[_builtins.bool]] = ..., environment_variables: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., iam_service_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., job_config: Optional[pulumi.Input[AppJobConfigArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., oauth_token: Optional[pulumi.Input[_builtins.str]] = ..., platform: Optional[pulumi.Input[_builtins.str]] = ..., production_branches: Optional[pulumi.Input[Sequence[pulumi.Input[AppProductionBranchArgs]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., repository: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @access_token.setter
    def access_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoBranchCreationConfig")
    def auto_branch_creation_config(self) -> Optional[pulumi.Input[AppAutoBranchCreationConfigArgs]]:
        
        ...
    
    @auto_branch_creation_config.setter
    def auto_branch_creation_config(self, value: Optional[pulumi.Input[AppAutoBranchCreationConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoBranchCreationPatterns")
    def auto_branch_creation_patterns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @auto_branch_creation_patterns.setter
    def auto_branch_creation_patterns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="basicAuthCredentials")
    def basic_auth_credentials(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @basic_auth_credentials.setter
    def basic_auth_credentials(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="buildSpec")
    def build_spec(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @build_spec.setter
    def build_spec(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheConfig")
    def cache_config(self) -> Optional[pulumi.Input[AppCacheConfigArgs]]:
        
        ...
    
    @cache_config.setter
    def cache_config(self, value: Optional[pulumi.Input[AppCacheConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeRoleArn")
    def compute_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @compute_role_arn.setter
    def compute_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customHeaders")
    def custom_headers(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @custom_headers.setter
    def custom_headers(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRules")
    def custom_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AppCustomRuleArgs]]]]:
        
        ...
    
    @custom_rules.setter
    def custom_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AppCustomRuleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultDomain")
    def default_domain(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_domain.setter
    def default_domain(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAutoBranchCreation")
    def enable_auto_branch_creation(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_auto_branch_creation.setter
    def enable_auto_branch_creation(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableBasicAuth")
    def enable_basic_auth(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_basic_auth.setter
    def enable_basic_auth(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableBranchAutoBuild")
    def enable_branch_auto_build(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_branch_auto_build.setter
    def enable_branch_auto_build(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableBranchAutoDeletion")
    def enable_branch_auto_deletion(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_branch_auto_deletion.setter
    def enable_branch_auto_deletion(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @environment_variables.setter
    def environment_variables(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamServiceRoleArn")
    def iam_service_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @iam_service_role_arn.setter
    def iam_service_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobConfig")
    def job_config(self) -> Optional[pulumi.Input[AppJobConfigArgs]]:
        
        ...
    
    @job_config.setter
    def job_config(self, value: Optional[pulumi.Input[AppJobConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauthToken")
    def oauth_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @oauth_token.setter
    def oauth_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def platform(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @platform.setter
    def platform(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="productionBranches")
    def production_branches(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AppProductionBranchArgs]]]]:
        
        ...
    
    @production_branches.setter
    def production_branches(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AppProductionBranchArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def repository(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @repository.setter
    def repository(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


@pulumi.type_token("aws:amplify/app:App")
class App(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., access_token: Optional[pulumi.Input[_builtins.str]] = ..., auto_branch_creation_config: Optional[pulumi.Input[Union[AppAutoBranchCreationConfigArgs, AppAutoBranchCreationConfigArgsDict]]] = ..., auto_branch_creation_patterns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., basic_auth_credentials: Optional[pulumi.Input[_builtins.str]] = ..., build_spec: Optional[pulumi.Input[_builtins.str]] = ..., cache_config: Optional[pulumi.Input[Union[AppCacheConfigArgs, AppCacheConfigArgsDict]]] = ..., compute_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., custom_headers: Optional[pulumi.Input[_builtins.str]] = ..., custom_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AppCustomRuleArgs, AppCustomRuleArgsDict]]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., enable_auto_branch_creation: Optional[pulumi.Input[_builtins.bool]] = ..., enable_basic_auth: Optional[pulumi.Input[_builtins.bool]] = ..., enable_branch_auto_build: Optional[pulumi.Input[_builtins.bool]] = ..., enable_branch_auto_deletion: Optional[pulumi.Input[_builtins.bool]] = ..., environment_variables: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., iam_service_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., job_config: Optional[pulumi.Input[Union[AppJobConfigArgs, AppJobConfigArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., oauth_token: Optional[pulumi.Input[_builtins.str]] = ..., platform: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., repository: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: Optional[AppArgs] = ..., opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., access_token: Optional[pulumi.Input[_builtins.str]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., auto_branch_creation_config: Optional[pulumi.Input[Union[AppAutoBranchCreationConfigArgs, AppAutoBranchCreationConfigArgsDict]]] = ..., auto_branch_creation_patterns: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., basic_auth_credentials: Optional[pulumi.Input[_builtins.str]] = ..., build_spec: Optional[pulumi.Input[_builtins.str]] = ..., cache_config: Optional[pulumi.Input[Union[AppCacheConfigArgs, AppCacheConfigArgsDict]]] = ..., compute_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., custom_headers: Optional[pulumi.Input[_builtins.str]] = ..., custom_rules: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AppCustomRuleArgs, AppCustomRuleArgsDict]]]]] = ..., default_domain: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., enable_auto_branch_creation: Optional[pulumi.Input[_builtins.bool]] = ..., enable_basic_auth: Optional[pulumi.Input[_builtins.bool]] = ..., enable_branch_auto_build: Optional[pulumi.Input[_builtins.bool]] = ..., enable_branch_auto_deletion: Optional[pulumi.Input[_builtins.bool]] = ..., environment_variables: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., iam_service_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., job_config: Optional[pulumi.Input[Union[AppJobConfigArgs, AppJobConfigArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., oauth_token: Optional[pulumi.Input[_builtins.str]] = ..., platform: Optional[pulumi.Input[_builtins.str]] = ..., production_branches: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AppProductionBranchArgs, AppProductionBranchArgsDict]]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., repository: Optional[pulumi.Input[_builtins.str]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...) -> App:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoBranchCreationConfig")
    def auto_branch_creation_config(self) -> pulumi.Output[outputs.AppAutoBranchCreationConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="autoBranchCreationPatterns")
    def auto_branch_creation_patterns(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="basicAuthCredentials")
    def basic_auth_credentials(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="buildSpec")
    def build_spec(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cacheConfig")
    def cache_config(self) -> pulumi.Output[outputs.AppCacheConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="computeRoleArn")
    def compute_role_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customHeaders")
    def custom_headers(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customRules")
    def custom_rules(self) -> pulumi.Output[Optional[Sequence[outputs.AppCustomRule]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultDomain")
    def default_domain(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAutoBranchCreation")
    def enable_auto_branch_creation(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableBasicAuth")
    def enable_basic_auth(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableBranchAutoBuild")
    def enable_branch_auto_build(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableBranchAutoDeletion")
    def enable_branch_auto_deletion(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamServiceRoleArn")
    def iam_service_role_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="jobConfig")
    def job_config(self) -> pulumi.Output[outputs.AppJobConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauthToken")
    def oauth_token(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def platform(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="productionBranches")
    def production_branches(self) -> pulumi.Output[Sequence[outputs.AppProductionBranch]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def repository(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    


