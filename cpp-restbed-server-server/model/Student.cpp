/**
 * Swagger Student Management System - OpenAPI 3.0
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.11
 * 
 *
 * NOTE: This class is auto generated by OpenAPI-Generator 6.3.0-SNAPSHOT.
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */



#include "Student.h"

#include <string>
#include <vector>
#include <map>
#include <sstream>
#include <stdexcept>
#include <regex>
#include <boost/lexical_cast.hpp>
#include <boost/property_tree/ptree.hpp>
#include <boost/property_tree/json_parser.hpp>
#include "helpers.h"

using boost::property_tree::ptree;
using boost::property_tree::read_json;
using boost::property_tree::write_json;

namespace org {
namespace openapitools {
namespace server {
namespace model {

Student::Student(boost::property_tree::ptree const& pt)
{
        fromPropertyTree(pt);
}


std::string Student::toJsonString(bool prettyJson /* = false */) const
{
	std::stringstream ss;
	write_json(ss, this->toPropertyTree(), prettyJson);
    // workaround inspired by: https://stackoverflow.com/a/56395440
    std::regex reg("\\\"([0-9]+\\.{0,1}[0-9]*)\\\"");
    std::string result = std::regex_replace(ss.str(), reg, "$1");
    return result;
}

void Student::fromJsonString(std::string const& jsonString)
{
	std::stringstream ss(jsonString);
	ptree pt;
	read_json(ss,pt);
	this->fromPropertyTree(pt);
}

ptree Student::toPropertyTree() const
{
	ptree pt;
	ptree tmp_node;
	pt.put("id", m_Id);
	pt.put("name", m_Name);
	pt.put("address", m_Address);
	pt.put("email", m_Email);
	pt.put("phone", m_Phone);
	return pt;
}

void Student::fromPropertyTree(ptree const &pt)
{
	ptree tmp_node;
	m_Id = pt.get("id", 0L);
	m_Name = pt.get("name", "");
	m_Address = pt.get("address", "");
	m_Email = pt.get("email", "");
	m_Phone = pt.get("phone", "");
}

int64_t Student::getId() const
{
    return m_Id;
}

void Student::setId(int64_t value)
{
    m_Id = value;
}


std::string Student::getName() const
{
    return m_Name;
}

void Student::setName(std::string value)
{
    m_Name = value;
}


std::string Student::getAddress() const
{
    return m_Address;
}

void Student::setAddress(std::string value)
{
    m_Address = value;
}


std::string Student::getEmail() const
{
    return m_Email;
}

void Student::setEmail(std::string value)
{
    m_Email = value;
}


std::string Student::getPhone() const
{
    return m_Phone;
}

void Student::setPhone(std::string value)
{
    m_Phone = value;
}



std::vector<Student> createStudentVectorFromJsonString(const std::string& json)
{
    std::stringstream sstream(json);
    boost::property_tree::ptree pt;
    boost::property_tree::json_parser::read_json(sstream,pt);

    auto vec = std::vector<Student>();
    for (const auto& child: pt) {
        vec.emplace_back(Student(child.second));
    }

    return vec;
}

}
}
}
}

