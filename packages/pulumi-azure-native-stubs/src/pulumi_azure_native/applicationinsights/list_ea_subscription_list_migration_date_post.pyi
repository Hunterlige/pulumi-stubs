

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ListEASubscriptionListMigrationDatePostResult', ..., 'list_ea_subscription_list_migration_date_post', ...]
@pulumi.output_type
class ListEASubscriptionListMigrationDatePostResult:
    
    def __init__(__self__, is_grand_fatherable_subscription=..., opted_in_date=...) -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isGrandFatherableSubscription")
    def is_grand_fatherable_subscription(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="optedInDate")
    def opted_in_date(self) -> Optional[_builtins.str]:
        
        ...
    


class AwaitableListEASubscriptionListMigrationDatePostResult(ListEASubscriptionListMigrationDatePostResult):
    def __await__(self): # -> Generator[Never, Any, ListEASubscriptionListMigrationDatePostResult]:
        ...
    


def list_ea_subscription_list_migration_date_post(opts: Optional[pulumi.InvokeOptions] = ...) -> AwaitableListEASubscriptionListMigrationDatePostResult:
    
    ...

def list_ea_subscription_list_migration_date_post_output(opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...) -> pulumi.Output[ListEASubscriptionListMigrationDatePostResult]:
    
    ...

