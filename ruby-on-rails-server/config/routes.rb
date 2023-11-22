=begin
Code Generation API

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 1.0.0
Generated by: https://github.com/openapitools/openapi-generator.git

=end
Rails.application.routes.draw do

  def add_openapi_route http_method, path, opts = {}
    full_path = path.gsub(/{(.*?)}/, ':\1')
    match full_path, to: "#{opts.fetch(:controller_name)}##{opts[:action_name]}", via: http_method
  end

  add_openapi_route 'POST', '/v1/apigen/generate/code', controller_name: 'default', action_name: 'generate_code_post'
end
