import streamlit as st
from duckduckgo_search import DDGS

st.set_page_config(page_title="Trợ Lý Văn Học Chuyên Sâu", page_icon="📚")

st.title("📚 Trợ Lý Văn Học (Phiên bản Ổn Định)")
st.caption("Sử dụng AI cao cấp để phân tích tác phẩm chính xác")

# Ô nhập liệu
noi_dung = st.text_area("Dán đoạn văn cần phân tích:", height=300)

if st.button("🚀 Bắt đầu phân tích"):
    if not noi_dung:
        st.warning("Vui lòng nhập nội dung trước!")
    else:
        with st.spinner("AI đang suy nghĩ kỹ để tránh nhầm lẫn..."):
            try:
                # Prompt yêu cầu AI tập trung tối đa vào văn bản
                prompt = f"""
                Bạn là một chuyên gia phê bình văn học Việt Nam giàu kinh nghiệm.
                Nhiệm vụ: Phân tích sâu sắc đoạn trích sau: "{noi_dung}"
                Yêu cầu:
                1. Phải xác định chính xác tên tác phẩm và tác giả. Không được nhầm lẫn nhân vật (ví dụ: không nhầm Lão Hạc sang Chí Phèo).
                2. Phân tích các biện pháp nghệ thuật và tâm trạng nhân vật bám sát văn bản.
                3. Trình bày bằng Markdown chuyên nghiệp, dễ đọc.
                """
                
                # Gọi AI miễn phí thông qua DuckDuckGo (Dùng model GPT-4o-mini hoặc Claude-3)
                with DDGS() as ddgs:
                    response = ddgs.chat(prompt, model='gpt-4o-mini')
                    st.markdown(response)
                    st.success("Đã hoàn tất phân tích chính xác!")
            except Exception as e:
                st.error("Server AI đang bận một chút, bạn hãy nhấn lại nút phân tích nhé!")
