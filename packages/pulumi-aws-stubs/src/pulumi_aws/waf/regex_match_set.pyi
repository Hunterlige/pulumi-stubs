import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["RegexMatchSetArgs", "RegexMatchSet"]

@pulumi.input_type
class RegexMatchSetArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        regex_match_tuples: Optional[
            pulumi.Input[Sequence[pulumi.Input[RegexMatchSetRegexMatchTupleArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="regexMatchTuples")
    def regex_match_tuples(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[RegexMatchSetRegexMatchTupleArgs]]]
    ]: ...
    @regex_match_tuples.setter
    def regex_match_tuples(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[RegexMatchSetRegexMatchTupleArgs]]]
        ],
    ): ...

@pulumi.input_type
class _RegexMatchSetState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        regex_match_tuples: Optional[
            pulumi.Input[Sequence[pulumi.Input[RegexMatchSetRegexMatchTupleArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="regexMatchTuples")
    def regex_match_tuples(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[RegexMatchSetRegexMatchTupleArgs]]]
    ]: ...
    @regex_match_tuples.setter
    def regex_match_tuples(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[RegexMatchSetRegexMatchTupleArgs]]]
        ],
    ): ...

@pulumi.type_token("aws:waf/regexMatchSet:RegexMatchSet")
class RegexMatchSet(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        regex_match_tuples: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            RegexMatchSetRegexMatchTupleArgs,
                            RegexMatchSetRegexMatchTupleArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: Optional[RegexMatchSetArgs] = ...,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        regex_match_tuples: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            RegexMatchSetRegexMatchTupleArgs,
                            RegexMatchSetRegexMatchTupleArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
    ) -> RegexMatchSet: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="regexMatchTuples")
    def regex_match_tuples(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.RegexMatchSetRegexMatchTuple]]]: ...
