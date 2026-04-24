import streamlit as st
import requests

# Sử dụng một API endpoint miễn phí và công khai (Serverless)
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"

st.set_page_config(page_title="Trợ Lý Văn Học Chuẩn", page_icon="📖")
st.title("📖 Trợ Lý Văn Học Chuyên Sâu")
st.caption("Phiên bản sửa lỗi ảo giác - Phân tích chính xác tác phẩm")

noi_dung = st.text_area("Dán đoạn văn cần phân tích:", height=300, placeholder="Ví dụ: Đoạn trích Lão Hạc...")

if st.button("🚀 Phân tích ngay"):
    if not noi_dung:
        st.error("Bạn chưa nhập nội dung!")
    else:
        with st.spinner("AI đang đọc kỹ tác phẩm để tránh nhầm lẫn..."):
            try:
                # Prompt được tối ưu để AI không 'chém gió' sang tác phẩm khác
                prompt = f"<s>[INST] Bạn là chuyên gia văn học Việt Nam. Hãy phân tích đoạn văn sau một cách chính xác, tuyệt đối không nhầm lẫn nhân vật: {noi_dung} [/INST]</s>"
                
                # Gửi yêu cầu đi (Không cần Key nếu dùng lượng vừa phải)
                response = requests.post(API_URL, json={"inputs": prompt})
                result = response.json()
                
                if isinstance(result, list):
                    st.markdown(result[0]['generated_text'].split("[/INST]</s>")[-1])
                    st.success("Đã hoàn thành phân tích!")
                else:
                    st.error("AI đang nghỉ ngơi một chút, bạn bấm nút lại lần nữa nhé!")
            except:
                st.error("Có lỗi kết nối. Hãy thử lại sau vài giây.")
