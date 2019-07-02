# 在Web应用中，服务器把网页传给浏览器，实际上就是把网页的HTML代码发送给浏览器，让浏览器显示出来。
# 而浏览器和服务器之间的传输协议是HTTP，所以：
# HTML是一种用来定义网页的文本，会HTML，就可以编写网页；
# HTTP是在网络上传输HTML的协议，用于浏览器和服务器的通信。
# chrome按F12后，Elements显示网页的结构，Network显示浏览器和服务器的通信。

# HTTP请求
# 跟踪了新浪的首页，我们来总结一下HTTP请求的流程：
# 步骤1：浏览器首先向服务器发送HTTP请求，请求包括：
# 方法：GET还是POST，GET仅请求资源，POST会附带用户数据；
# 路径：/full/url/path；
# 域名：由Host头指定：Host: www.sina.com.cn
# 以及其他相关的Header；
# 如果是POST，那么请求还包括一个Body，包含用户数据。
# 步骤2：服务器向浏览器返回HTTP响应，响应包括：
# 响应代码：200表示成功，3xx表示重定向，4xx表示客户端发送的请求有错误，5xx表示服务器端处理时发生了错误；
# 响应类型：由Content-Type指定，例如：Content-Type: text/html;charset=utf-8表示响应类型是HTML文本，并且编码是UTF-8，
# Content-Type: image/jpeg表示响应类型是JPEG格式的图片；
# 以及其他相关的Header；
# 通常服务器的HTTP响应会携带内容，也就是有一个Body，包含响应的内容，网页的HTML源码就在Body中。
# 步骤3：如果浏览器还需要继续向服务器请求其他资源，比如图片，就再次发出HTTP请求，重复步骤1、2。
# Web采用的HTTP协议采用了非常简单的请求-响应模式，从而大大简化了开发。当我们编写一个页面时，我们只需要在HTTP响应中把HTML
# 发送出去，不需要考虑如何附带图片、视频等，浏览器如果需要请求图片和视频，一个HTTP请求只处理一个资源。

# HTTP格式
# 每个HTTP请求和响应都遵循相同的格式，一个HTTP包含Header和Body两部分，其中Body是可选的。
# HTTP响应如果包含body，也是通过\r\n\r\n来分隔的。请再次注意，Body的数据类型由Content-Type头来确定，
# 如果是网页，Body就是文本，如果是图片，Body就是图片的二进制数据。
# 当存在Content-Encoding时，Body数据是被压缩的，最常见的压缩方式是gzip，所以，看到Content-Encoding: gzip时，
# 需要将Body数据先解压缩，才能得到真正的数据。压缩的目的在于减少Body的大小，加快网络传输。
