import streamlit as st
from collections import Counter, defaultdict

st.set_page_config(page_title="Phân loại nhà đầu tư", layout="centered")

st.title("📊 Hệ thống phân loại nhà đầu tư & thiên kiến hành vi")

# =========================
# PHẦN 1
# =========================
st.header("Phần 1: Nhận diện loại nhà đầu tư")

questions_part1 = [
("1. Vai trò chính của Anh/Chị trong việc quản lý tiền bạc là:",
 ["A. Là người bảo vệ tài sản bằng cách không đầu tư rủi ro.",
  "B. Tích cực giao dịch để tích lũy tài sản.",
  "C. Nghiên cứu kỹ lưỡng trước khi đưa ra quyết định.",
  "D. Nghe theo lời khuyên của người khác."]),

("2. Khi nói đến các vấn đề tài chính, Anh/Chị đồng ý nhất với nhận định nào?",
 ["A. Mất tiền là kết quả tồi tệ nhất có thể xảy ra.",
  "B. Tôi nên hành động nhanh chóng khi có cơ hội kiếm tiền.",
  "C. Tôi cần dành thời gian để hiểu rõ khoản đầu tư dù có thể lỡ cơ hội.",
  "D. Tôi không nên là người trực tiếp giám sát tiền của mình."]),

("3. Khi quyết định đầu tư, Anh/Chị tin tưởng vào lời khuyên của:",
 ["A. Kỷ luật tự giác của bản thân.",
  "B. Bản năng của mình.",
  "C. Kết quả nghiên cứu của riêng tôi.",
  "D. Một người nào đó không phải là tôi."]),

("4. Khi thị trường đi lên, Anh/Chị cảm thấy:",
 ["A. Nhẹ nhõm.",
  "B. Phấn khích.",
  "C. Bình tĩnh và lý trí.",
  "D. Vui vì mình đã làm theo lời khuyên của ai đó."]),

("5. Trong lĩnh vực tài chính, từ nào mô tả đúng nhất về Anh/Chị?",
 ["A. Người bảo vệ (Guardian).",
  "B. Người giao dịch (Trader).",
  "C. Người nghiên cứu (Researcher).",
  "D. Người nghe theo lời khuyên (Advice-taker)."]),

("6. Về việc tuân thủ một kế hoạch quản lý tiền bạc:",
 ["A. Tôi sẽ làm nếu nó giúp bảo vệ tài sản của mình.",
  "B. Việc theo kế hoạch không quá quan trọng.",
  "C. Kế hoạch là tốt, nhưng quyết định phải bao gồm suy nghĩ của bản thân.",
  "D. Tôi có xu hướng nghe theo lời khuyên của người khác."]),

("7. Anh/Chị cảm thấy tự tin nhất về tiền bạc khi:",
 ["A. Có thể ngủ ngon khi biết tài sản được đầu tư an toàn.",
  "B. Đầu tư vào các tài sản có tiềm năng tăng giá cao.",
  "C. Tự đưa ra quyết định hoặc ít nhất là đóng góp ý kiến.",
  "D. Đầu tư vào những thứ mà nhiều người khác cũng đầu tư."]),

("8. Khi một người bạn gợi ý một ý tưởng đầu tư 'chắc ăn':",
 ["A. Tôi thường tránh những loại ý tưởng này.",
  "B. Tôi yêu thích chúng và có thể hành động ngay.",
  "C. Tôi sẽ tự nghiên cứu rồi mới quyết định.",
  "D. Tôi cần hỏi ý kiến người khác trước khi quyết định."]),

("9. Biến động ngắn hạn trong danh mục khiến Anh/Chị:",
 ["A. Hoảng sợ và nghĩ đến việc bán.",
  "B. Thấy cơ hội và nghĩ đến việc mua.",
  "C. Thấy mình vẫn kiểm soát được và có thể không làm gì cả.",
  "D. Muốn gọi cho ai đó để xem tiền của mình thế nào."]),

("10. Nếu tham gia một trận đá bóng, Anh/Chị đóng vai trò nào?",
 ["A. Cầu thủ phòng ngự.",
  "B. Cầu thủ tấn công.",
  "C. Chiến lược gia/Huấn luyện viên.",
  "D. Người hâm mộ."])
]

answers_part1 = []

for i, (q, opts) in enumerate(questions_part1):
    ans = st.radio(q, opts, key=f"q{i}")
    answers_part1.append(ans[0])

# =========================
# PHẦN 2
# =========================
st.header("Phần 2: Đánh giá thiên kiến hành vi")

st.markdown("""
**Thang đo Likert:**
1 - Rất không đồng ý  
2 - Không đồng ý  
3 - Phân vân  
4 - Đồng ý  
5 - Rất đồng ý  
""")

questions_part2 = [
("Lệch lạc neo quyết định (Anchoring)", "11. Khi định bán một khoản đầu tư, giá tôi đã mua là yếu tố lớn tôi cân nhắc."),
("Tâm lý sợ thua lỗ (Loss Aversion)", "12. Nỗi đau mất tiền mạnh gấp ít nhất 2 lần niềm vui kiếm được tiền."),
("Lệch lạc thiếu kiểm soát (Self-control)", "13. Tôi sẽ mua những thứ mình muốn ngay cả khi chúng không phải lựa chọn tài chính tốt nhất."),
("Tâm lý hối tiếc (Regret)", "14. Những quyết định tài chính sai lầm trong quá khứ khiến tôi thay đổi quyết định hiện tại."),
("Hiệu ứng sở hữu (Endowment)", "15. Đôi khi tôi gắn bó với một số khoản đầu tư khiến tôi không nỡ bán chúng."),
("Lệch lạc sẵn có (Availability)", "16. Tôi thường hành động ngay với một khoản đầu tư mới nếu thấy nó hợp lý."),
("Thành kiến tự quy kết (Self-attribution)", "17. Tôi thấy các đầu tư thành công là do tôi, còn thất bại là do lời khuyên người khác."),
("Thành kiến giữ nguyên hiện trạng (Status quo)", "18. Khi định thay đổi danh mục, tôi suy nghĩ nhiều nhưng thường ít thay đổi gì cả."),
("Quá tự tin (Overconfidence)", "19. Tôi tin rằng kiến thức đầu tư của mình trên mức trung bình."),
("Lệch lạc khung tâm lý (Framing)", "20. Tôi tin lời khuyên từ các công ty lớn quảng cáo nhiều hơn."),
("Thành kiến bảo thủ (Conservatism)", "21. Tôi không dễ dàng thay đổi quan điểm về các khoản đầu tư."),
("Thành kiến yêu thích (Affinity)", "22. Tôi đầu tư vào công ty phản ánh giá trị cá nhân."),
("Hạch toán tâm trí (Mental Accounting)", "23. Tôi chia khoản đầu tư vào các tài khoản riêng."),
("Thành kiến nhận thức muộn (Hindsight)", "24. Khi nhìn lại sai lầm, tôi thấy chúng dễ tránh."),
("Thành kiến đại diện (Representativeness)", "25. Lựa chọn dựa vào các trường hợp tương tự trong quá khứ."),
("Thành kiến kết quả (Outcome)", "26. Quan trọng nhất là kiếm được tiền."),
("Bất hòa nhận thức (Cognitive Dissonance)", "27. Tôi tập trung vào mặt tích cực hơn là rủi ro."),
("Ảo tưởng kiểm soát (Illusion of Control)", "28. Tôi tin mình kiểm soát được kết quả."),
("Thành kiến xác nhận (Confirmation)", "29. Tôi tìm thông tin để xác nhận quyết định của mình."),
("Lệch lạc gần đây (Recency)", "30. Tôi coi trọng kết quả gần đây hơn lịch sử dài hạn.")
]

answers_part2 = defaultdict(list)

likert_labels = {
    1: "1 - Rất không đồng ý",
    2: "2 - Không đồng ý",
    3: "3 - Phân vân",
    4: "4 - Đồng ý",
    5: "5 - Rất đồng ý"
}

for i, (bias, q) in enumerate(questions_part2):
    val = st.radio(q, list(likert_labels.keys()),
                   format_func=lambda x: likert_labels[x],
                   key=f"b{i}")
    answers_part2[bias].append(val)

# =========================
# KẾT QUẢ
# =========================
if st.button("📌 Xem kết quả"):

    count = Counter(answers_part1)

    if count["A"] >= 5:
        investor_type = "Preserver"
    elif count["B"] >= 5:
        investor_type = "Accumulator"
    elif count["C"] >= 5:
        investor_type = "Independent"
    elif count["D"] >= 5:
        investor_type = "Follower"
    else:
        investor_type = "Không xác định rõ"

    st.subheader(f"👉 Loại nhà đầu tư: {investor_type}")

    # Thiên kiến
    biases_detected = [b for b, v in answers_part2.items() if max(v) >= 4]

    st.subheader("👉 Thiên kiến hành vi nổi bật:")
    if biases_detected:
        for b in biases_detected:
            st.write(f"- {b}")
    else:
        st.write("Không phát hiện rõ")

    # Khuyến nghị đầy đủ
    st.subheader("👉 Khuyến nghị:")

    recommendations = {
        "Preserver": """
**Chiến lược tư vấn:** Tập trung mục tiêu bảo vệ tài sản dài hạn  
**Phân bổ tài sản:** Danh mục thận trọng, ít biến động  
**Tiếp cận:** Huấn luyện tâm lý để tránh hoảng loạn khi thị trường giảm
""",
        "Accumulator": """
**Chiến lược tư vấn:** Kiểm soát sự tự tin và định hướng dài hạn  
**Phân bổ tài sản:** Tránh danh mục quá rủi ro  
**Tiếp cận:** Giám sát giao dịch và kỷ luật tài chính
""",
        "Independent": """
**Chiến lược tư vấn:** Đóng vai trò phản biện khách quan  
**Phân bổ tài sản:** Danh mục kỷ luật  
**Tiếp cận:** Giáo dục để giảm thiên kiến xác nhận
""",
        "Follower": """
**Chiến lược tư vấn:** Tập trung giáo dục tài chính  
**Phân bổ tài sản:** Đa dạng hóa danh mục  
**Tiếp cận:** Tránh chạy theo xu hướng thị trường
"""
    }

    st.info(recommendations.get(investor_type, "Chưa có khuyến nghị"))