import streamlit as st
from collections import Counter, defaultdict

st.set_page_config(page_title="Phân loại nhà đầu tư", layout="centered")

st.title("📊 Hệ thống phân loại nhà đầu tư & thiên kiến hành vi")

# =========================
# PHẦN 1: 10 câu hỏi phân loại
# =========================
st.header("Phần 1: Nhận diện loại nhà đầu tư")

questions_part1 = [
    ("1. Vai trò chính của bạn trong quản lý tiền?",
     ["A. Bảo vệ tài sản, tránh rủi ro",
      "B. Tích cực giao dịch để tích lũy",
      "C. Nghiên cứu kỹ trước khi quyết định",
      "D. Nghe theo lời khuyên người khác"]),

    ("2. Khi nói đến tài chính?",
     ["A. Mất tiền là tệ nhất",
      "B. Nắm bắt cơ hội nhanh",
      "C. Hiểu rõ trước khi đầu tư",
      "D. Không nên tự quản lý"]),

    ("3. Khi đầu tư, bạn tin vào?",
     ["A. Kỷ luật bản thân",
      "B. Bản năng",
      "C. Nghiên cứu cá nhân",
      "D. Người khác"]),

    ("4. Khi thị trường tăng?",
     ["A. Nhẹ nhõm",
      "B. Phấn khích",
      "C. Bình tĩnh",
      "D. Vui vì nghe theo người khác"]),

    ("5. Bạn là người?",
     ["A. Người bảo vệ",
      "B. Người giao dịch",
      "C. Người nghiên cứu",
      "D. Người nghe theo"]),

    ("6. Tuân thủ kế hoạch?",
     ["A. Có nếu bảo vệ tài sản",
      "B. Không quan trọng",
      "C. Có nhưng cần suy nghĩ riêng",
      "D. Nghe theo người khác"]),

    ("7. Khi nào bạn tự tin?",
     ["A. Khi an toàn",
      "B. Khi cơ hội cao",
      "C. Khi tự quyết định",
      "D. Khi nhiều người cùng đầu tư"]),

    ("8. Ý tưởng đầu tư chắc ăn?",
     ["A. Tránh",
      "B. Hành động ngay",
      "C. Nghiên cứu trước",
      "D. Hỏi người khác"]),

    ("9. Khi danh mục biến động?",
     ["A. Hoảng sợ",
      "B. Thấy cơ hội",
      "C. Bình tĩnh",
      "D. Hỏi ý kiến"]),

    ("10. Vai trò trong bóng đá?",
     ["A. Phòng ngự",
      "B. Tấn công",
      "C. Chiến lược",
      "D. Khán giả"]),
]

answers_part1 = []

for i, (q, opts) in enumerate(questions_part1):
    ans = st.radio(q, opts, key=f"q{i}")
    answers_part1.append(ans[0])  # lấy A/B/C/D

# =========================
# PHẦN 2: 20 câu hỏi thiên kiến
# =========================
st.header("Phần 2: Đánh giá thiên kiến hành vi")

st.markdown("**Chọn mức độ từ 1 đến 5:**")
st.markdown("""
1 - Hoàn toàn không đồng ý  
2 - Không đồng ý  
3 - Phân vân  
4 - Đồng ý  
5 - Hoàn toàn đồng ý  
""")

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

answers_part2 = defaultdict(list)

for i, (bias, q) in enumerate(questions_part2):
    val = st.radio(
        q,
        [1, 2, 3, 4, 5],
        format_func=lambda x: {
            1: "1 - Hoàn toàn không đồng ý",
            2: "2 - Không đồng ý",
            3: "3 - Phân vân",
            4: "4 - Đồng ý",
            5: "5 - Hoàn toàn đồng ý"
        }[x],
        key=f"b{i}"
    )
    answers_part2[bias].append(val)

# =========================
# XỬ LÝ KẾT QUẢ
# =========================
if st.button("📌 Xem kết quả"):

    # -------- Phân loại --------
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

    # -------- Thiên kiến --------
    biases_detected = [
        bias for bias, values in answers_part2.items()
        if max(values) >= 4
    ]

    st.subheader("👉 Thiên kiến hành vi nổi bật:")

    if biases_detected:
        for b in biases_detected:
            st.write(f"- {b}")
    else:
        st.write("Không phát hiện thiên kiến rõ ràng")

    # -------- Khuyến nghị --------
    st.subheader("👉 Khuyến nghị:")

    recommendations = {
        "Preserver": "Ưu tiên an toàn, danh mục thận trọng, tránh hoảng loạn khi thị trường biến động.",
        "Accumulator": "Kiểm soát rủi ro, tránh giao dịch quá mức, cần kỷ luật dài hạn.",
        "Independent": "Cần phản biện khách quan, tránh thiên kiến xác nhận.",
        "Follower": "Tăng cường kiến thức, tránh chạy theo xu hướng."
    }

    st.info(recommendations.get(investor_type, "Chưa có khuyến nghị phù hợp."))