/*
Code Generation API

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

API version: 1.0.0
*/

// Code generated by OpenAPI Generator (https://openapi-generator.tech); DO NOT EDIT.

package openapi

import (
	"encoding/json"
)

// checks if the GenerateCodePost400Response type satisfies the MappedNullable interface at compile time
var _ MappedNullable = &GenerateCodePost400Response{}

// GenerateCodePost400Response struct for GenerateCodePost400Response
type GenerateCodePost400Response struct {
	// A message indicating that the request was invalid
	Message *string `json:"message,omitempty"`
}

// NewGenerateCodePost400Response instantiates a new GenerateCodePost400Response object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewGenerateCodePost400Response() *GenerateCodePost400Response {
	this := GenerateCodePost400Response{}
	return &this
}

// NewGenerateCodePost400ResponseWithDefaults instantiates a new GenerateCodePost400Response object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewGenerateCodePost400ResponseWithDefaults() *GenerateCodePost400Response {
	this := GenerateCodePost400Response{}
	return &this
}

// GetMessage returns the Message field value if set, zero value otherwise.
func (o *GenerateCodePost400Response) GetMessage() string {
	if o == nil || isNil(o.Message) {
		var ret string
		return ret
	}
	return *o.Message
}

// GetMessageOk returns a tuple with the Message field value if set, nil otherwise
// and a boolean to check if the value has been set.
func (o *GenerateCodePost400Response) GetMessageOk() (*string, bool) {
	if o == nil || isNil(o.Message) {
		return nil, false
	}
	return o.Message, true
}

// HasMessage returns a boolean if a field has been set.
func (o *GenerateCodePost400Response) HasMessage() bool {
	if o != nil && !isNil(o.Message) {
		return true
	}

	return false
}

// SetMessage gets a reference to the given string and assigns it to the Message field.
func (o *GenerateCodePost400Response) SetMessage(v string) {
	o.Message = &v
}

func (o GenerateCodePost400Response) MarshalJSON() ([]byte, error) {
	toSerialize,err := o.ToMap()
	if err != nil {
		return []byte{}, err
	}
	return json.Marshal(toSerialize)
}

func (o GenerateCodePost400Response) ToMap() (map[string]interface{}, error) {
	toSerialize := map[string]interface{}{}
	if !isNil(o.Message) {
		toSerialize["message"] = o.Message
	}
	return toSerialize, nil
}

type NullableGenerateCodePost400Response struct {
	value *GenerateCodePost400Response
	isSet bool
}

func (v NullableGenerateCodePost400Response) Get() *GenerateCodePost400Response {
	return v.value
}

func (v *NullableGenerateCodePost400Response) Set(val *GenerateCodePost400Response) {
	v.value = val
	v.isSet = true
}

func (v NullableGenerateCodePost400Response) IsSet() bool {
	return v.isSet
}

func (v *NullableGenerateCodePost400Response) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableGenerateCodePost400Response(val *GenerateCodePost400Response) *NullableGenerateCodePost400Response {
	return &NullableGenerateCodePost400Response{value: val, isSet: true}
}

func (v NullableGenerateCodePost400Response) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableGenerateCodePost400Response) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}

