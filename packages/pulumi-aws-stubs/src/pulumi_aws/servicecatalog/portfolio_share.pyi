

import builtins as _builtins
import sys
import pulumi
from typing import Optional, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['PortfolioShareArgs', 'PortfolioShare']
@pulumi.input_type
class PortfolioShareArgs:
    def __init__(__self__, *, portfolio_id: pulumi.Input[_builtins.str], principal_id: pulumi.Input[_builtins.str], type: pulumi.Input[_builtins.str], accept_language: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., share_principals: Optional[pulumi.Input[_builtins.bool]] = ..., share_tag_options: Optional[pulumi.Input[_builtins.bool]] = ..., wait_for_acceptance: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="portfolioId")
    def portfolio_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @portfolio_id.setter
    def portfolio_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @principal_id.setter
    def principal_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceptLanguage")
    def accept_language(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @accept_language.setter
    def accept_language(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharePrincipals")
    def share_principals(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @share_principals.setter
    def share_principals(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shareTagOptions")
    def share_tag_options(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @share_tag_options.setter
    def share_tag_options(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitForAcceptance")
    def wait_for_acceptance(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @wait_for_acceptance.setter
    def wait_for_acceptance(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.input_type
class _PortfolioShareState:
    def __init__(__self__, *, accept_language: Optional[pulumi.Input[_builtins.str]] = ..., accepted: Optional[pulumi.Input[_builtins.bool]] = ..., portfolio_id: Optional[pulumi.Input[_builtins.str]] = ..., principal_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., share_principals: Optional[pulumi.Input[_builtins.bool]] = ..., share_tag_options: Optional[pulumi.Input[_builtins.bool]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., wait_for_acceptance: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceptLanguage")
    def accept_language(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @accept_language.setter
    def accept_language(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def accepted(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @accepted.setter
    def accepted(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="portfolioId")
    def portfolio_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @portfolio_id.setter
    def portfolio_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @principal_id.setter
    def principal_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharePrincipals")
    def share_principals(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @share_principals.setter
    def share_principals(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="shareTagOptions")
    def share_tag_options(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @share_tag_options.setter
    def share_tag_options(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitForAcceptance")
    def wait_for_acceptance(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @wait_for_acceptance.setter
    def wait_for_acceptance(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


@pulumi.type_token("aws:servicecatalog/portfolioShare:PortfolioShare")
class PortfolioShare(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., accept_language: Optional[pulumi.Input[_builtins.str]] = ..., portfolio_id: Optional[pulumi.Input[_builtins.str]] = ..., principal_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., share_principals: Optional[pulumi.Input[_builtins.bool]] = ..., share_tag_options: Optional[pulumi.Input[_builtins.bool]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., wait_for_acceptance: Optional[pulumi.Input[_builtins.bool]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: PortfolioShareArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., accept_language: Optional[pulumi.Input[_builtins.str]] = ..., accepted: Optional[pulumi.Input[_builtins.bool]] = ..., portfolio_id: Optional[pulumi.Input[_builtins.str]] = ..., principal_id: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., share_principals: Optional[pulumi.Input[_builtins.bool]] = ..., share_tag_options: Optional[pulumi.Input[_builtins.bool]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ..., wait_for_acceptance: Optional[pulumi.Input[_builtins.bool]] = ...) -> PortfolioShare:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceptLanguage")
    def accept_language(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def accepted(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="portfolioId")
    def portfolio_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sharePrincipals")
    def share_principals(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="shareTagOptions")
    def share_tag_options(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="waitForAcceptance")
    def wait_for_acceptance(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    


