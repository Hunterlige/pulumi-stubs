

import builtins as _builtins
import sys
import pulumi

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetRouterConfigurationRouterResult']
@pulumi.output_type
class GetRouterConfigurationRouterResult(dict):
    def __init__(__self__, *, platform: _builtins.str, router_type_identifier: _builtins.str, software: _builtins.str, vendor: _builtins.str, xslt_template_name: _builtins.str, xslt_template_name_for_mac_sec: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def platform(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="routerTypeIdentifier")
    def router_type_identifier(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def software(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def vendor(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="xsltTemplateName")
    def xslt_template_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="xsltTemplateNameForMacSec")
    def xslt_template_name_for_mac_sec(self) -> _builtins.str:
        ...
    


