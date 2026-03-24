import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["V2modelsSlotArgs", "V2modelsSlot"]

@pulumi.input_type
class V2modelsSlotArgs:
    def __init__(
        __self__,
        *,
        bot_id: pulumi.Input[_builtins.str],
        bot_version: pulumi.Input[_builtins.str],
        intent_id: pulumi.Input[_builtins.str],
        locale_id: pulumi.Input[_builtins.str],
        value_elicitation_setting: pulumi.Input[
            V2modelsSlotValueElicitationSettingArgs
        ],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        multiple_values_settings: Optional[
            pulumi.Input[Sequence[pulumi.Input[V2modelsSlotMultipleValuesSettingArgs]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        obfuscation_settings: Optional[
            pulumi.Input[Sequence[pulumi.Input[V2modelsSlotObfuscationSettingArgs]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        slot_type_id: Optional[pulumi.Input[_builtins.str]] = ...,
        sub_slot_settings: Optional[
            pulumi.Input[Sequence[pulumi.Input[V2modelsSlotSubSlotSettingArgs]]]
        ] = ...,
        timeouts: Optional[pulumi.Input[V2modelsSlotTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="botId")
    def bot_id(self) -> pulumi.Input[_builtins.str]: ...
    @bot_id.setter
    def bot_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="botVersion")
    def bot_version(self) -> pulumi.Input[_builtins.str]: ...
    @bot_version.setter
    def bot_version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="intentId")
    def intent_id(self) -> pulumi.Input[_builtins.str]: ...
    @intent_id.setter
    def intent_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="localeId")
    def locale_id(self) -> pulumi.Input[_builtins.str]: ...
    @locale_id.setter
    def locale_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="valueElicitationSetting")
    def value_elicitation_setting(
        self,
    ) -> pulumi.Input[V2modelsSlotValueElicitationSettingArgs]: ...
    @value_elicitation_setting.setter
    def value_elicitation_setting(
        self, value: pulumi.Input[V2modelsSlotValueElicitationSettingArgs]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="multipleValuesSettings")
    def multiple_values_settings(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[V2modelsSlotMultipleValuesSettingArgs]]]
    ]: ...
    @multiple_values_settings.setter
    def multiple_values_settings(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[V2modelsSlotMultipleValuesSettingArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="obfuscationSettings")
    def obfuscation_settings(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[V2modelsSlotObfuscationSettingArgs]]]
    ]: ...
    @obfuscation_settings.setter
    def obfuscation_settings(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[V2modelsSlotObfuscationSettingArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="slotTypeId")
    def slot_type_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @slot_type_id.setter
    def slot_type_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subSlotSettings")
    def sub_slot_settings(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[V2modelsSlotSubSlotSettingArgs]]]
    ]: ...
    @sub_slot_settings.setter
    def sub_slot_settings(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[V2modelsSlotSubSlotSettingArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[V2modelsSlotTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[V2modelsSlotTimeoutsArgs]]): ...

@pulumi.input_type
class _V2modelsSlotState:
    def __init__(
        __self__,
        *,
        bot_id: Optional[pulumi.Input[_builtins.str]] = ...,
        bot_version: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        intent_id: Optional[pulumi.Input[_builtins.str]] = ...,
        locale_id: Optional[pulumi.Input[_builtins.str]] = ...,
        multiple_values_settings: Optional[
            pulumi.Input[Sequence[pulumi.Input[V2modelsSlotMultipleValuesSettingArgs]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        obfuscation_settings: Optional[
            pulumi.Input[Sequence[pulumi.Input[V2modelsSlotObfuscationSettingArgs]]]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        slot_id: Optional[pulumi.Input[_builtins.str]] = ...,
        slot_type_id: Optional[pulumi.Input[_builtins.str]] = ...,
        sub_slot_settings: Optional[
            pulumi.Input[Sequence[pulumi.Input[V2modelsSlotSubSlotSettingArgs]]]
        ] = ...,
        timeouts: Optional[pulumi.Input[V2modelsSlotTimeoutsArgs]] = ...,
        value_elicitation_setting: Optional[
            pulumi.Input[V2modelsSlotValueElicitationSettingArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="botId")
    def bot_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bot_id.setter
    def bot_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="botVersion")
    def bot_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @bot_version.setter
    def bot_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="intentId")
    def intent_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @intent_id.setter
    def intent_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="localeId")
    def locale_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @locale_id.setter
    def locale_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="multipleValuesSettings")
    def multiple_values_settings(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[V2modelsSlotMultipleValuesSettingArgs]]]
    ]: ...
    @multiple_values_settings.setter
    def multiple_values_settings(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[V2modelsSlotMultipleValuesSettingArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="obfuscationSettings")
    def obfuscation_settings(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[V2modelsSlotObfuscationSettingArgs]]]
    ]: ...
    @obfuscation_settings.setter
    def obfuscation_settings(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[V2modelsSlotObfuscationSettingArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="slotId")
    def slot_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @slot_id.setter
    def slot_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="slotTypeId")
    def slot_type_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @slot_type_id.setter
    def slot_type_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="subSlotSettings")
    def sub_slot_settings(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[V2modelsSlotSubSlotSettingArgs]]]
    ]: ...
    @sub_slot_settings.setter
    def sub_slot_settings(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[V2modelsSlotSubSlotSettingArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[V2modelsSlotTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[V2modelsSlotTimeoutsArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="valueElicitationSetting")
    def value_elicitation_setting(
        self,
    ) -> Optional[pulumi.Input[V2modelsSlotValueElicitationSettingArgs]]: ...
    @value_elicitation_setting.setter
    def value_elicitation_setting(
        self, value: Optional[pulumi.Input[V2modelsSlotValueElicitationSettingArgs]]
    ): ...

@pulumi.type_token("aws:lex/v2modelsSlot:V2modelsSlot")
class V2modelsSlot(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        bot_id: Optional[pulumi.Input[_builtins.str]] = ...,
        bot_version: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        intent_id: Optional[pulumi.Input[_builtins.str]] = ...,
        locale_id: Optional[pulumi.Input[_builtins.str]] = ...,
        multiple_values_settings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            V2modelsSlotMultipleValuesSettingArgs,
                            V2modelsSlotMultipleValuesSettingArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        obfuscation_settings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            V2modelsSlotObfuscationSettingArgs,
                            V2modelsSlotObfuscationSettingArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        slot_type_id: Optional[pulumi.Input[_builtins.str]] = ...,
        sub_slot_settings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            V2modelsSlotSubSlotSettingArgs,
                            V2modelsSlotSubSlotSettingArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        timeouts: Optional[
            pulumi.Input[Union[V2modelsSlotTimeoutsArgs, V2modelsSlotTimeoutsArgsDict]]
        ] = ...,
        value_elicitation_setting: Optional[
            pulumi.Input[
                Union[
                    V2modelsSlotValueElicitationSettingArgs,
                    V2modelsSlotValueElicitationSettingArgsDict,
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: V2modelsSlotArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        bot_id: Optional[pulumi.Input[_builtins.str]] = ...,
        bot_version: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        intent_id: Optional[pulumi.Input[_builtins.str]] = ...,
        locale_id: Optional[pulumi.Input[_builtins.str]] = ...,
        multiple_values_settings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            V2modelsSlotMultipleValuesSettingArgs,
                            V2modelsSlotMultipleValuesSettingArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        obfuscation_settings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            V2modelsSlotObfuscationSettingArgs,
                            V2modelsSlotObfuscationSettingArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        slot_id: Optional[pulumi.Input[_builtins.str]] = ...,
        slot_type_id: Optional[pulumi.Input[_builtins.str]] = ...,
        sub_slot_settings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            V2modelsSlotSubSlotSettingArgs,
                            V2modelsSlotSubSlotSettingArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        timeouts: Optional[
            pulumi.Input[Union[V2modelsSlotTimeoutsArgs, V2modelsSlotTimeoutsArgsDict]]
        ] = ...,
        value_elicitation_setting: Optional[
            pulumi.Input[
                Union[
                    V2modelsSlotValueElicitationSettingArgs,
                    V2modelsSlotValueElicitationSettingArgsDict,
                ]
            ]
        ] = ...,
    ) -> V2modelsSlot: ...
    @_builtins.property
    @pulumi.getter(name="botId")
    def bot_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="botVersion")
    def bot_version(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="intentId")
    def intent_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="localeId")
    def locale_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="multipleValuesSettings")
    def multiple_values_settings(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.V2modelsSlotMultipleValuesSetting]]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="obfuscationSettings")
    def obfuscation_settings(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.V2modelsSlotObfuscationSetting]]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="slotId")
    def slot_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="slotTypeId")
    def slot_type_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="subSlotSettings")
    def sub_slot_settings(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.V2modelsSlotSubSlotSetting]]]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.V2modelsSlotTimeouts]]: ...
    @_builtins.property
    @pulumi.getter(name="valueElicitationSetting")
    def value_elicitation_setting(
        self,
    ) -> pulumi.Output[outputs.V2modelsSlotValueElicitationSetting]: ...
