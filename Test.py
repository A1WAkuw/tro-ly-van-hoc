import streamlit as st
import wikipedia
from g4f.client import Client

# Khởi tạo Client
client = Client()
wikipedia.set_lang("vi")

# Hàm lấy ảnh minh họa
def get_wiki_image(search_query):
    try:
        titles = wikipedia.search(search_query, results=1)
        if titles:
            page = wikipedia.page(titles[0])
            return page.images[0] if page.images else None
    except: return None
    return None

# --- SIDEBAR ĐIỀU HƯỚNG ---
st.sidebar.title("🎮 Menu Chức Năng")
app_mode = st.sidebar.selectbox("Chọn chế độ phân tích:", ["📚 Phân tích Văn học", "🌍 Nghị luận Xã hội"])

# --- TRANG 1: PHÂN TÍCH VĂN HỌC ---
if app_mode == "📚 Phân tích Văn học":
    st.title("📚 Trợ Lý Văn Học Chuyên Sâu")
    st.info("Chế độ này tập trung vào tác giả, tác phẩm và nghệ thuật ngôn từ.")
    
    noi_dung = st.text_area("Dán đoạn văn học cần phân tích:", height=250)
    
    if st.button("🚀 Phân tích Văn học"):
        if noi_dung:
            col1, col2 = st.columns([1, 2])
            with st.spinner("Đang xử lý..."):
                # Gọi AI xác định tác phẩm để lấy ảnh
                detect = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": f"Tên tác phẩm chính trong đoạn này là gì? Chỉ trả về tên: {noi_dung[:200]}"}])
                ten_tp = detect.choices[0].message.content
                img = get_wiki_image(ten_tp)
                
                with col1:
                    if img: st.image(img, caption=f"Minh họa: {ten_tp}")
                with col2:
                    prompt = f"Phân tích sâu sắc đoạn văn học này, bám sát nghệ thuật và tâm trạng nhân vật, không nhầm tác phẩm: {noi_dung}"
                    res = client.chat.completions.create(model="gpt-4", messages=[{"role": "user", "content": prompt}])
                    st.markdown(res.choices[0].message.content)

# --- TRANG 2: NGHỊ LUẬN XÃ HỘI ---
elif app_mode == "🌍 Nghị luận Xã hội":
    st.title("🌍 Phân Tích Vấn Đề Xã Hội")
    st.info("Chế độ này giúp bạn lập dàn ý, phân tích các hiện tượng đời sống, tư tưởng đạo lý.")
    
    van_de = st.text_input("Nhập vấn đề xã hội cần bàn luận:", placeholder="Ví dụ: Áp lực đồng lứa, Rác thải nhựa, Lòng hiếu thảo...")
    
    if st.button("💡 Phân tích vấn đề"):
        if van_de:
            with st.spinner("AI đang tổng hợp góc nhìn xã hội..."):
                prompt_xh = f"""
                Bạn là một chuyên gia xã hội học. Hãy viết bài nghị luận xã hội về vấn đề: "{van_de}"
                Yêu cầu:
                1. Nêu hiện trạng và nguyên nhân.
                2. Phân tích tác động tích cực/tiêu cực.
                3. Đưa ra dẫn chứng thực tế (người thật, việc thật).
                4. Giải pháp và bài học nhận thức.
                Trình bày bằng các đề mục rõ ràng, súc tích.
                """
                res_xh = client.chat.completions.create(model="gpt-4", messages=[{"role": "user", "content": prompt_xh}])
                
                st.subheader(f"📊 Góc nhìn về: {van_de}")
                st.markdown(res_xh.choices[0].message.content)
                st.balloons() # Hiệu ứng chúc mừng khi xong bài nghị luận
