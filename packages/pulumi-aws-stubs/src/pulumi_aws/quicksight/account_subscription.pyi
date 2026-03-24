

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, overload

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AccountSubscriptionArgs', 'AccountSubscription']
@pulumi.input_type
class AccountSubscriptionArgs:
    def __init__(__self__, *, account_name: pulumi.Input[_builtins.str], authentication_method: pulumi.Input[_builtins.str], edition: pulumi.Input[_builtins.str], notification_email: pulumi.Input[_builtins.str], active_directory_name: Optional[pulumi.Input[_builtins.str]] = ..., admin_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., admin_pro_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., author_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., author_pro_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., aws_account_id: Optional[pulumi.Input[_builtins.str]] = ..., contact_number: Optional[pulumi.Input[_builtins.str]] = ..., directory_id: Optional[pulumi.Input[_builtins.str]] = ..., email_address: Optional[pulumi.Input[_builtins.str]] = ..., first_name: Optional[pulumi.Input[_builtins.str]] = ..., iam_identity_center_instance_arn: Optional[pulumi.Input[_builtins.str]] = ..., last_name: Optional[pulumi.Input[_builtins.str]] = ..., reader_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., reader_pro_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., realm: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @account_name.setter
    def account_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationMethod")
    def authentication_method(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @authentication_method.setter
    def authentication_method(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def edition(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @edition.setter
    def edition(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationEmail")
    def notification_email(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @notification_email.setter
    def notification_email(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeDirectoryName")
    def active_directory_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @active_directory_name.setter
    def active_directory_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminGroups")
    def admin_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @admin_groups.setter
    def admin_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminProGroups")
    def admin_pro_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @admin_pro_groups.setter
    def admin_pro_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorGroups")
    def author_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @author_groups.setter
    def author_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorProGroups")
    def author_pro_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @author_pro_groups.setter
    def author_pro_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @aws_account_id.setter
    def aws_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactNumber")
    def contact_number(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @contact_number.setter
    def contact_number(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @directory_id.setter
    def directory_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @email_address.setter
    def email_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firstName")
    def first_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @first_name.setter
    def first_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamIdentityCenterInstanceArn")
    def iam_identity_center_instance_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @iam_identity_center_instance_arn.setter
    def iam_identity_center_instance_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastName")
    def last_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_name.setter
    def last_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="readerGroups")
    def reader_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @reader_groups.setter
    def reader_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="readerProGroups")
    def reader_pro_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @reader_pro_groups.setter
    def reader_pro_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def realm(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @realm.setter
    def realm(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _AccountSubscriptionState:
    def __init__(__self__, *, account_name: Optional[pulumi.Input[_builtins.str]] = ..., account_subscription_status: Optional[pulumi.Input[_builtins.str]] = ..., active_directory_name: Optional[pulumi.Input[_builtins.str]] = ..., admin_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., admin_pro_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., authentication_method: Optional[pulumi.Input[_builtins.str]] = ..., author_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., author_pro_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., aws_account_id: Optional[pulumi.Input[_builtins.str]] = ..., contact_number: Optional[pulumi.Input[_builtins.str]] = ..., directory_id: Optional[pulumi.Input[_builtins.str]] = ..., edition: Optional[pulumi.Input[_builtins.str]] = ..., email_address: Optional[pulumi.Input[_builtins.str]] = ..., first_name: Optional[pulumi.Input[_builtins.str]] = ..., iam_identity_center_instance_arn: Optional[pulumi.Input[_builtins.str]] = ..., last_name: Optional[pulumi.Input[_builtins.str]] = ..., notification_email: Optional[pulumi.Input[_builtins.str]] = ..., reader_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., reader_pro_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., realm: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @account_name.setter
    def account_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountSubscriptionStatus")
    def account_subscription_status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @account_subscription_status.setter
    def account_subscription_status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeDirectoryName")
    def active_directory_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @active_directory_name.setter
    def active_directory_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminGroups")
    def admin_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @admin_groups.setter
    def admin_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminProGroups")
    def admin_pro_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @admin_pro_groups.setter
    def admin_pro_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationMethod")
    def authentication_method(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @authentication_method.setter
    def authentication_method(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorGroups")
    def author_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @author_groups.setter
    def author_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorProGroups")
    def author_pro_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @author_pro_groups.setter
    def author_pro_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @aws_account_id.setter
    def aws_account_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactNumber")
    def contact_number(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @contact_number.setter
    def contact_number(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @directory_id.setter
    def directory_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def edition(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @edition.setter
    def edition(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @email_address.setter
    def email_address(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="firstName")
    def first_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @first_name.setter
    def first_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamIdentityCenterInstanceArn")
    def iam_identity_center_instance_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @iam_identity_center_instance_arn.setter
    def iam_identity_center_instance_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastName")
    def last_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_name.setter
    def last_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationEmail")
    def notification_email(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @notification_email.setter
    def notification_email(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="readerGroups")
    def reader_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @reader_groups.setter
    def reader_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="readerProGroups")
    def reader_pro_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @reader_pro_groups.setter
    def reader_pro_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def realm(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @realm.setter
    def realm(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token(...)
class AccountSubscription(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., account_name: Optional[pulumi.Input[_builtins.str]] = ..., active_directory_name: Optional[pulumi.Input[_builtins.str]] = ..., admin_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., admin_pro_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., authentication_method: Optional[pulumi.Input[_builtins.str]] = ..., author_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., author_pro_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., aws_account_id: Optional[pulumi.Input[_builtins.str]] = ..., contact_number: Optional[pulumi.Input[_builtins.str]] = ..., directory_id: Optional[pulumi.Input[_builtins.str]] = ..., edition: Optional[pulumi.Input[_builtins.str]] = ..., email_address: Optional[pulumi.Input[_builtins.str]] = ..., first_name: Optional[pulumi.Input[_builtins.str]] = ..., iam_identity_center_instance_arn: Optional[pulumi.Input[_builtins.str]] = ..., last_name: Optional[pulumi.Input[_builtins.str]] = ..., notification_email: Optional[pulumi.Input[_builtins.str]] = ..., reader_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., reader_pro_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., realm: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AccountSubscriptionArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., account_name: Optional[pulumi.Input[_builtins.str]] = ..., account_subscription_status: Optional[pulumi.Input[_builtins.str]] = ..., active_directory_name: Optional[pulumi.Input[_builtins.str]] = ..., admin_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., admin_pro_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., authentication_method: Optional[pulumi.Input[_builtins.str]] = ..., author_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., author_pro_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., aws_account_id: Optional[pulumi.Input[_builtins.str]] = ..., contact_number: Optional[pulumi.Input[_builtins.str]] = ..., directory_id: Optional[pulumi.Input[_builtins.str]] = ..., edition: Optional[pulumi.Input[_builtins.str]] = ..., email_address: Optional[pulumi.Input[_builtins.str]] = ..., first_name: Optional[pulumi.Input[_builtins.str]] = ..., iam_identity_center_instance_arn: Optional[pulumi.Input[_builtins.str]] = ..., last_name: Optional[pulumi.Input[_builtins.str]] = ..., notification_email: Optional[pulumi.Input[_builtins.str]] = ..., reader_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., reader_pro_groups: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., realm: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ...) -> AccountSubscription:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountSubscriptionStatus")
    def account_subscription_status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="activeDirectoryName")
    def active_directory_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminGroups")
    def admin_groups(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="adminProGroups")
    def admin_pro_groups(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authenticationMethod")
    def authentication_method(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorGroups")
    def author_groups(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="authorProGroups")
    def author_pro_groups(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="awsAccountId")
    def aws_account_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contactNumber")
    def contact_number(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="directoryId")
    def directory_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def edition(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="firstName")
    def first_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="iamIdentityCenterInstanceArn")
    def iam_identity_center_instance_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastName")
    def last_name(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationEmail")
    def notification_email(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readerGroups")
    def reader_groups(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="readerProGroups")
    def reader_pro_groups(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def realm(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


