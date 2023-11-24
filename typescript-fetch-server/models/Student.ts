/* tslint:disable */
/* eslint-disable */
/**
 * Swagger Student Management System - OpenAPI 3.0
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.11
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { exists, mapValues } from '../runtime';
/**
 * 
 * @export
 * @interface Student
 */
export interface Student {
    /**
     * 
     * @type {number}
     * @memberof Student
     */
    id?: number;
    /**
     * 
     * @type {string}
     * @memberof Student
     */
    name?: string;
    /**
     * 
     * @type {string}
     * @memberof Student
     */
    address?: string;
    /**
     * 
     * @type {string}
     * @memberof Student
     */
    email?: string;
    /**
     * 
     * @type {string}
     * @memberof Student
     */
    phone?: string;
}

/**
 * Check if a given object implements the Student interface.
 */
export function instanceOfStudent(value: object): boolean {
    let isInstance = true;

    return isInstance;
}

export function StudentFromJSON(json: any): Student {
    return StudentFromJSONTyped(json, false);
}

export function StudentFromJSONTyped(json: any, ignoreDiscriminator: boolean): Student {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'id': !exists(json, 'id') ? undefined : json['id'],
        'name': !exists(json, 'name') ? undefined : json['name'],
        'address': !exists(json, 'address') ? undefined : json['address'],
        'email': !exists(json, 'email') ? undefined : json['email'],
        'phone': !exists(json, 'phone') ? undefined : json['phone'],
    };
}

export function StudentToJSON(value?: Student | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'id': value.id,
        'name': value.name,
        'address': value.address,
        'email': value.email,
        'phone': value.phone,
    };
}

