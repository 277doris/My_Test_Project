import com.bcloud.msg.http.HttpSender;

public class HttpSenderTest {

	public static void main(String[] args) {
		String uri = "http://localhost/msg/HttpBatchSendSM";//应用地址
		String account = "test";//账号
		String pswd = "test";//密码
		String mobiles = "13800210021,13800138000";//手机号码，多个号码使用","分割
		String content = "测试";//短信内容
		boolean needstatus = true;//是否需要状态报告，需要true，不需要false
		String product = "";//产品ID
		String extno = "";//扩展码
		String respType = "json";//返回json格式响应
		boolean encrypt = true;// 密码使用时间戳加密
		try {
			String returnString = HttpSender.send(uri, account, pswd, mobiles, content, needstatus, product, extno, respType, encrypt);
			System.out.println(returnString);
			//TODO 处理返回值,参见HTTP协议文档
		} catch (Exception e) {
			//TODO 处理异常
			e.printStackTrace();
		}
	}
}
