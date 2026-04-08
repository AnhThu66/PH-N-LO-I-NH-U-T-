import streamlit as st

st.set_page_config(page_title="Phân loại nhà đầu tư", layout="centered")

st.title("📊 Hệ thống phân loại nhà đầu tư & thiên kiến hành vi")

# =========================
# PHẦN 1: 10 câu hỏi phân loại
# =========================
st.header("Phần 1: Nhận diện loại nhà đầu tư")

questions_part1 = [
    "1. Vai trò chính của bạn trong quản lý tiền?",
    "2. Khi nói đến tài chính, bạn đồng ý nhất với điều nào?",
    "3. Bạn tin tưởng vào điều gì khi đầu tư?",
    "4. Khi thị trường tăng, bạn cảm thấy?",
    "5. Từ nào mô tả bạn nhất?",
    "6. Bạn tuân thủ kế hoạch tài chính thế nào?",
    "7. Khi nào bạn tự tin nhất?",
    "8. Khi có ý tưởng đầu tư 'chắc ăn'?",
    "9. Khi danh mục biến động?",
    "10. Vai trò của bạn trong trận bóng?"
]

options = ["A", "B", "C", "D"]

answers_part1 = []

for i, q in enumerate(questions_part1):
    ans = st.radio(q, options, key=f"q{i}")
    answers_part1.append(ans)

# =========================
# PHẦN 2: 20 câu hỏi thiên kiến
# =========================
st.header("Phần 2: Đánh giá thiên kiến hành vi")

questions_part2 = [
    ("Anchoring", "11. Giá mua ảnh hưởng quyết định bán"),
    ("Loss Aversion", "12. Sợ mất tiền hơn kiếm tiền"),
    ("Self-control", "13. Mua dù không hợp lý"),
    ("Regret", "14. Bị ảnh hưởng bởi sai lầm cũ"),
    ("Endowment", "15. Không muốn bán tài sản"),
    ("Availability", "16. Hành động ngay khi thấy hợp lý"),
    ("Self-attribution", "17. Thành công do mình, thất bại do người khác"),
    ("Status quo", "18. Ít thay đổi danh mục"),
    ("Overconfidence", "19. Tin mình giỏi hơn trung bình"),
    ("Framing", "20. Tin công ty lớn quảng cáo"),
    ("Conservatism", "21. Không dễ đổi quan điểm"),
    ("Affinity", "22. Đầu tư theo sở thích cá nhân"),
    ("Mental Accounting", "23. Chia tiền thành nhiều tài khoản"),
    ("Hindsight", "24. Nghĩ sai lầm trước dễ tránh"),
    ("Representativeness", "25. Dựa vào quá khứ tương tự"),
    ("Outcome", "26. Chỉ quan tâm kiếm tiền"),
    ("Cognitive Dissonance", "27. Tập trung mặt tích cực"),
    ("Illusion of Control", "28. Tin mình kiểm soát được"),
    ("Confirmation", "29. Tìm thông tin xác nhận"),
    ("Recency", "30. Quan trọng kết quả gần đây")
]

likert = [1, 2, 3, 4, 5]

answers_part2 = {}

for i, (bias, q) in enumerate(questions_part2):
    val = st.slider(q, 1, 5, 3, key=f"b{i}")
    answers_part2[bias] = val

# =========================
# XỬ LÝ KẾT QUẢ
# =========================
if st.button("📌 Xem kết quả"):

    # -------- Phân loại nhà đầu tư --------
    from collections import Counter
    count = Counter(answers_part1)

    investor_type = None

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

    # -------- Thiên kiến --------
    biases_detected = [bias for bias, val in answers_part2.items() if val >= 4]

    st.subheader("👉 Thiên kiến hành vi nổi bật:")
    if biases_detected:
        for b in biases_detected:
            st.write(f"- {b}")
    else:
        st.write("Không phát hiện thiên kiến rõ ràng")

    # -------- Khuyến nghị --------
    st.subheader("👉 Khuyến nghị:")

    recommendations = {
        "Preserver": "Ưu tiên an toàn, danh mục thận trọng, cần huấn luyện để tránh hoảng loạn khi thị trường biến động.",
        "Accumulator": "Kiểm soát rủi ro, tránh giao dịch quá mức, cần kỷ luật và định hướng dài hạn.",
        "Independent": "Cần phản biện khách quan, tránh thiên kiến xác nhận, duy trì kỷ luật danh mục.",
        "Follower": "Tăng cường kiến thức, tránh chạy theo xu hướng, tập trung chiến lược dài hạn."
    }

    st.info(recommendations.get(investor_type, "Chưa có khuyến nghị phù hợp."))