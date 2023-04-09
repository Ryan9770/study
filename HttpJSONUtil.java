public static String requestJson(String action, HashMap<String, String> header, String method, String encoding, HashMap<String, String> params) {

        String result = "";

        try {
            URL url = new URL(action); // URL 객체 생성
            HttpURLConnection http = (HttpURLConnection) url.openConnection(); // HttpURLConnection로 action에서 받은 url에 Connetion 생성

            http.setDefaultUseCaches(false);    // cache false
            http.setDoInput(true);              // inputstream으로 데이터 수신
            http.setDoOutput(true);             // outputstream으로 데이터 송신
            http.setRequestMethod(method);      // GET, POST, ... method 설정
            http.setRequestProperty("Content-Type", "application/json; charset=UTF-8"); // header 설정
            http.setRequestProperty("Accept", "application/json");   // header 설정
            
            if(header != null) {  // header 존재 시
            	Set<String> headerKey = header.keySet(); // HashMap 속의 key Set collection으로 변환 
                for(Iterator<String> headerIterator = headerKey.iterator(); headerIterator.hasNext();) { // key가 있을때마다
                	String hk = (String) headerIterator.next(); // key
                    String hv = header.get(hk);   // value
                	http.setRequestProperty(hk, hv); // header 설정
                }
            }
            
            ObjectMapper mapper = new ObjectMapper(); // Jackson ObjectMapper 객체생성
            String param = mapper.writeValueAsString(params); // HashMap<String, String> 형태의 데이터를 key=value 형식의 String형으로 변환
            System.out.println(">>>>>>>>api_param: "+param); // 확인
            OutputStreamWriter outStream = new OutputStreamWriter(http.getOutputStream(), encoding); // OutputStreamWriter 객체생성
            PrintWriter writer = new PrintWriter(outStream); // PrintWriter(OutputStream) 객체 생성
            writer.write(param); // parameter 출력
            writer.flush(); // 스트림 플러시

            InputStreamReader tmp = new InputStreamReader(http.getInputStream(), encoding); // InputStreamReader 객체 생성
            BufferedReader reader = new BufferedReader(tmp); // BufferedReader 객체 생성
            StringBuilder builder = new StringBuilder(); // StringBuilder 객체 생성
            String str;
            
            while ((str = reader.readLine()) != null) { // 개행단위가 null이 아닐경우
                builder.append(str + "\n"); // builder에 BufferedReader에서 읽어온 데이터를 string으로 변환하여 입력
            }
            
            result = builder.toString(); // result를 return 타입에 맞게 변환
            System.out.println("result :"+result);
            
            return result;

        } catch (MalformedURLException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
        
        return result;
    }
