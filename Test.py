import streamlit as st
from g4f.client import Client

# Khởi tạo Client không cần Key
client = Client()

st.set_page_config(page_title="Trợ Lý Văn Học Chuẩn", page_icon="📚")
st.title("📚 Trợ Lý Văn Học (Bản Fix Lỗi)")

noi_dung = st.text_area("Dán đoạn văn cần phân tích:", height=300, placeholder="Nhập văn bản tại đây...")

if st.button("🚀 Phân tích chính xác"):
    if not noi_dung:
        st.warning("Vui lòng nhập nội dung!")
    else:
        with st.spinner("AI đang đọc kỹ để tránh nhầm lẫn tác phẩm..."):
            try:
                # Prompt này ép AI phải phân tích đúng chi tiết văn bản
                prompt = f"""
                Bạn là một chuyên gia phê bình văn học Việt Nam.
                Nhiệm vụ: Phân tích đoạn trích sau: "{noi_dung}"
                Yêu cầu nghiêm ngặt:
                1. Xác định đúng tác phẩm và tác giả. Không được nhầm lẫn nhân vật.
                2. Phân tích dựa trên các từ ngữ cụ thể trong đoạn trích.
                3. Nêu bật nghệ thuật đặc sắc và tâm trạng nhân vật.
                """
                
                response = client.chat.completions.create(
                    model="gpt-4", # Hoặc gpt-3.5-turbo nếu gpt-4 chậm
                    messages=[{"role": "user", "content": prompt}],
                )
                
                ket_qua = response.choices[0].message.content
                st.markdown(ket_qua)
                st.success("Đã hoàn tất phân tích bám sát nội dung!")
            except Exception as e:
                st.error("Server đang bận một chút, bạn hãy nhấn lại nút nhé!")
