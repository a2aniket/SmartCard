=begin
#Code Generation API

#No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

The version of the OpenAPI document: 1.0.0

Generated by: https://openapi-generator.tech
OpenAPI Generator version: 6.3.0-SNAPSHOT

=end

require 'cgi'

module OpenapiClient
  class DefaultApi
    attr_accessor :api_client

    def initialize(api_client = ApiClient.default)
      @api_client = api_client
    end
    # Generate code from OpenAPI specification
    # @param generate_code_post_request [GenerateCodePostRequest] 
    # @param [Hash] opts the optional parameters
    # @return [GenerateCodePost200Response]
    def generate_code_post(generate_code_post_request, opts = {})
      data, _status_code, _headers = generate_code_post_with_http_info(generate_code_post_request, opts)
      data
    end

    # Generate code from OpenAPI specification
    # @param generate_code_post_request [GenerateCodePostRequest] 
    # @param [Hash] opts the optional parameters
    # @return [Array<(GenerateCodePost200Response, Integer, Hash)>] GenerateCodePost200Response data, response status code and response headers
    def generate_code_post_with_http_info(generate_code_post_request, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: DefaultApi.generate_code_post ...'
      end
      # verify the required parameter 'generate_code_post_request' is set
      if @api_client.config.client_side_validation && generate_code_post_request.nil?
        fail ArgumentError, "Missing the required parameter 'generate_code_post_request' when calling DefaultApi.generate_code_post"
      end
      # resource path
      local_var_path = '/generate/code'

      # query parameters
      query_params = opts[:query_params] || {}

      # header parameters
      header_params = opts[:header_params] || {}
      # HTTP header 'Accept' (if needed)
      header_params['Accept'] = @api_client.select_header_accept(['application/json'])
      # HTTP header 'Content-Type'
      content_type = @api_client.select_header_content_type(['application/json'])
      if !content_type.nil?
          header_params['Content-Type'] = content_type
      end

      # form parameters
      form_params = opts[:form_params] || {}

      # http body (model)
      post_body = opts[:debug_body] || @api_client.object_to_http_body(generate_code_post_request)

      # return_type
      return_type = opts[:debug_return_type] || 'GenerateCodePost200Response'

      # auth_names
      auth_names = opts[:debug_auth_names] || []

      new_options = opts.merge(
        :operation => :"DefaultApi.generate_code_post",
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:POST, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: DefaultApi#generate_code_post\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end
  end
end
