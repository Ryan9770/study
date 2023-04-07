import java.util.Map;

import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

@RestController
public class APIController {

	 @PostMapping("/api")
	    public ResponseEntity<String> handleDynamicRequest(@RequestBody Map<String, Object> requestParams) {
	        String url = (String) requestParams.get("url");
	        Map<String, Object> params = (Map<String, Object>) requestParams.get("params");
	        String method = (String) requestParams.get("method");

	        RestTemplate restTemplate = new RestTemplate();
	        HttpHeaders headers = new HttpHeaders();
	        headers.setContentType(MediaType.APPLICATION_JSON);

	        HttpEntity<Map<String, Object>> entity = new HttpEntity<>(params, headers);
	        ResponseEntity<String> response;

	        if (method.equals("GET")) {
	            String queryString = buildQueryString(params);
	            String urlWithParams = url + "?" + queryString;
	            response = restTemplate.getForEntity(urlWithParams, String.class);
	        } else if (method.equals("POST")) {
	            response = restTemplate.exchange(url, HttpMethod.POST, entity, String.class);
	        } else {
	            return ResponseEntity.badRequest().body("Invalid HTTP method: " + method);
	        }

	        return response;
	    }

	    private String buildQueryString(Map<String, Object> params) {
	        StringBuilder sb = new StringBuilder();
	        for (String key : params.keySet()) {
	            Object value = params.get(key);
	            if (value != null) {
	                if (sb.length() > 0) {
	                    sb.append("&");
	                }
	                sb.append(key).append("=").append(value.toString());
	            }
	        }
	        return sb.toString();
	    }
	

}
