import streamlit as st
import google.generativeai as genai

# Lấy Key từ mục Secrets bảo mật của Streamlit Cloud
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
except:
    st.error("Chưa cấu hình API Key trong phần Secrets!")

st.set_page_config(page_title="AI Văn Học Chuẩn 100%", page_icon="📚")
st.title("📚 Trợ Lý Văn Học Chuyên Sâu (Bản Chính Xác)")

noi_dung = st.text_area("Dán đoạn văn cần phân tích vào đây:", height=300)

if st.button("🚀 Phân tích chính xác"):
    if not noi_dung:
        st.warning("Bạn chưa nhập nội dung!")
    else:
        with st.spinner("AI đang đối soát dữ liệu văn học..."):
            try:
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                # Prompt này là "lệnh cưỡng chế" để AI không được nhầm lẫn
                prompt = f"""
                Bạn là một giáo viên dạy văn cấp 3 xuất sắc. 
                Nhiệm vụ: Phân tích đoạn trích sau: "{noi_dung}"
                Quy tắc nghiêm ngặt: 
                1. Tuyệt đối không được nhầm lẫn sang tác phẩm khác. Nếu là Lão Hạc thì chỉ nói về Lão Hạc, Chí Phèo chỉ nói về Chí Phèo.
                2. Phân tích chi tiết các từ ngữ, hình ảnh, biện pháp tu từ có TRONG ĐOẠN TRÍCH.
                3. Nêu bật giá trị nhân đạo và nghệ thuật miêu tả tâm lý.
                4. Nếu không rõ tác phẩm, hãy phân tích dựa trên nội dung chữ đã cung cấp, không tự đoán mò tác giả.
                """
                
                response = model.generate_content(prompt)
                st.markdown(response.text)
                st.success("Đã hoàn tất phân tích bám sát văn bản!")
            except Exception as e:
                st.error("Lỗi hệ thống hoặc API Key hết hạn. Hãy kiểm tra lại phần Secrets.")
