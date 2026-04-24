import streamlit as st
from g4f.client import Client
import wikipedia

# Khởi tạo Client g4f
client = Client()
wikipedia.set_lang("vi")

# --- SIDEBAR ĐIỀU HƯỚNG ---
st.sidebar.title("🎮 Menu Chức Năng")
app_mode = st.sidebar.selectbox("Chọn chế độ phân tích:", ["📚 Phân tích Văn học", "🌍 Nghị luận Xã hội"])

# --- TRANG 1: PHÂN TÍCH VĂN HỌC ---
if app_mode == "📚 Phân tích Văn học":
    st.title("📚 Trợ Lý Văn Học Chuyên Sâu")
    st.info("Chế độ này tập trung vào tác giả, tác phẩm và nghệ thuật.")
    
    noi_dung = st.text_area("Dán đoạn văn học cần phân tích:", height=250)
    
    if st.button("🚀 Phân tích Văn học"):
        if noi_dung:
            with st.spinner("AI đang xử lý (Không dùng API Key)..."):
                try:
                    # Prompt ép AI bám sát văn bản để không nhầm Lão Hạc/Chí Phèo
                    prompt = f"""
                    Nhiệm vụ: Phân tích đoạn văn sau một cách chính xác. 
                    Yêu cầu: Xác định đúng tác giả, tác phẩm. Tuyệt đối không nhầm nhân vật.
                    Nội dung: {noi_dung}
                    """
                    
                    # Ép dùng các Provider ổn định nhất để tránh lỗi RetryProviderError
                    response = client.chat.completions.create(
                        model="gpt-4",
                        messages=[{"role": "user", "content": prompt}]
                    )
                    
                    st.subheader("📝 Kết quả phân tích")
                    st.markdown(response.choices[0].message.content)
                except Exception as e:
                    st.error("Máy chủ AI đang bận, bạn hãy nhấn nút lại một lần nữa nhé!")

# --- TRANG 2: NGHỊ LUẬN XÃ HỘI ---
elif app_mode == "🌍 Nghị luận Xã hội":
    st.title("🌍 Phân Tích Vấn Đề Xã Hội")
    st.info("Chế độ này giúp bạn lập dàn ý và phân tích thực tế đời sống.")
    
    van_de = st.text_input("Nhập vấn đề xã hội (Ví dụ: Áp lực học tập, Tình bạn...):")
    
    if st.button("💡 Phân tích vấn đề"):
        if van_de:
            with st.spinner("AI đang tổng hợp góc nhìn xã hội..."):
                try:
                    prompt_xh = f"Hãy viết bài nghị luận xã hội về: {van_de}. Yêu cầu: Có hiện trạng, dẫn chứng và giải pháp."
                    
                    response_xh = client.chat.completions.create(
                        model="gpt-4o",
                        messages=[{"role": "user", "content": prompt_xh}]
                    )
                    
                    st.subheader(f"📊 Phân tích: {van_de}")
                    st.markdown(response_xh.choices[0].message.content)
                    st.balloons()
                except:
                    st.error("Server đang bảo trì, vui lòng thử lại sau vài giây.")
