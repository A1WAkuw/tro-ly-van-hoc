import streamlit as st
from g4f.client import Client

# Khởi tạo AI Client (Hoàn toàn miễn phí, không cần Key)
client = Client()

st.set_page_config(page_title="AI Văn Học Không Key", page_icon="🖋️", layout="wide")

st.title("🖋️ Trợ Lý Văn Học Chuyên Sâu (Free AI)")
st.caption("Sử dụng công nghệ GPT-4 miễn phí để phân tích tác phẩm.")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📝 Nội dung cần phân tích")
    noi_dung = st.text_area("Dán đoạn trích hoặc đề bài:", height=350, 
                             placeholder="Ví dụ: Phân tích đoạn trích Lão Hạc...")
    muc_do = st.select_slider("Độ chi tiết:", options=["Sơ lược", "Đầy đủ", "Chuyên sâu HSG"])
    nut_chay = st.button("🚀 Bắt đầu phân tích", use_container_width=True)

if nut_chay:
    if not noi_dung:
        st.warning("Vui lòng nhập nội dung!")
    else:
        with col2:
            st.subheader("✨ Kết quả phân tích")
            with st.spinner("AI đang 'cảm thụ' văn bản..."):
                try:
                    # Lệnh gửi cho AI (Prompt Engineering)
                    cau_lenh = f"""
                    Bạn là một chuyên gia phê bình văn học. Hãy phân tích {muc_do} đoạn sau: {noi_dung}
                    Yêu cầu: 
                    1. Chỉ rõ các từ ngữ, hình ảnh đắt giá.
                    2. Phân tích các biện pháp nghệ thuật và tác dụng của chúng.
                    3. Làm rõ tư tưởng, tình cảm của tác giả.
                    4. Trình bày bằng Markdown, in đậm các ý quan trọng.
                    """
                    
                    # Gọi AI chạy
                    response = client.chat.completions.create(
                        model="gpt-4",
                        messages=[{"role": "user", "content": cau_lenh}],
                    )
                    
                    ket_qua = response.choices[0].message.content
                    st.markdown(ket_qua)
                    st.success("Hoàn tất phân tích!")
                except Exception as e:
                    st.error(f"Lỗi hệ thống: {e}")
                    st.info("Thử lại sau vài giây nếu server bận nhé!")