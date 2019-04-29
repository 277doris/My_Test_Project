package java.jsoupt;
Runnable runnable = new Runnable() {
        @Override
        public void run() {
            Connection conn = Jsoup.connect(url);
            // �޸�http���е�header,αװ�����������ץȡ
            conn.header("User-Agent", userAgent);
            Document doc = null;
            try {
                doc = conn.get();
            } catch (IOException e) {
                e.printStackTrace();
            }
            //��ȡ���ݵ�����
            Element elementDiv = doc.getElementById("shop-all-list");
            Elements elementsUl = elementDiv.getElementsByTag("ul");
            Elements elements = elementsUl.first().getElementsByTag("li");
            for (Element element : elements) {
                Elements elements1 = element.children();
                String targetUrl = elements1.get(0).getElementsByTag("a").attr("href");

                String img = elements1.get(0).getElementsByTag("img").first().attr("data-src");
                if (img.contains(".jpg")) {
                    int a = img.indexOf(".jpg");
                    img = img.substring(0, a + 4);
                }

                String radiumName = elements1.get(1).child(0).getElementsByTag("h4").text();
                String address0 = elements1.get(1).child(2).getElementsByTag("a").get(1).text();

                String address1 = elements1.get(1).child(2).getElementsByClass("addr").text();

                RadiumBean radiumBean = new RadiumBean();
                radiumBean.setImg(img);
                radiumBean.setName(radiumName);
                radiumBean.setAddress(address0 + " " + address1);
                list.add(radiumBean);
            }
            // ִ����Ϻ��handler����һ������Ϣ
            Message message = new Message();
            message.arg1 = Integer.parseInt(curPage);
            handler.sendMessage(message);

        }
    };