

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['GetPortfolioConstraintsResult', 'AwaitableGetPortfolioConstraintsResult', 'get_portfolio_constraints', 'get_portfolio_constraints_output']
@pulumi.output_type
class GetPortfolioConstraintsResult:
    
    def __init__(__self__, accept_language=..., details=..., id=..., portfolio_id=..., product_id=..., region=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="acceptLanguage")
    def accept_language(self) -> Optional[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def details(self) -> Sequence[outputs.GetPortfolioConstraintsDetailResult]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="portfolioId")
    def portfolio_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="productId")
    def product_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str:
        ...
    


class AwaitableGetPortfolioConstraintsResult(GetPortfolioConstraintsResult):
    def __await__(self): # -> Generator[Never, Any, GetPortfolioConstraintsResult]:
        ...
    


def get_portfolio_constraints(accept_language: Optional[_builtins.str] = ..., portfolio_id: Optional[_builtins.str] = ..., product_id: Optional[_builtins.str] = ..., region: Optional[_builtins.str] = ..., opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableGetPortfolioConstraintsResult:
    
    ...

def get_portfolio_constraints_output(accept_language: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., portfolio_id: Optional[pulumi.Input[_builtins.str]] = ..., product_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., region: Optional[pulumi.Input[Optional[_builtins.str]]] = ..., opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[GetPortfolioConstraintsResult]:
    
    ...

