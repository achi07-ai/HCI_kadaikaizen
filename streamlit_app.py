import streamlit as st
import random

# --- ページ設定 ---
st.set_page_config(page_title="教科書販売 公式サイト", layout="centered")

# --- スタイル設定 ---
st.markdown("""
    <style>
    /* 明確な「ステップ表示」のデザイン */
    .step-container {
        background-color: #f8f9fa;
        border-left: 5px solid #28a745;
        padding: 15px;
        margin: 10px 0;
        border-radius: 5px;
    }
    .step-number {
        font-weight: bold;
        color: #28a745;
        margin-right: 10px;
    }
    
    /* 入力フォームの視認性向上 */
    .stTextInput input {
        border: 1px solid #ced4da !important;
        background-color: white !important;
    }
    
    /* 予約番号を目立たせるスタイル */
    .rsv-number {
        font-size: 1.5rem;
        font-weight: bold;
        color: #155724;
        background-color: #d4edda;
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #c3e6cb;
        display: inline-block;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ページ遷移と状態の管理 ---
if 'page' not in st.session_state:
    st.session_state.page = 'good_step1'
if 'rsv_num' not in st.session_state:
    st.session_state.rsv_num = None  # 予約番号を保持する変数

# --- 改善版：ご利用の流れ ---
if st.session_state.page == 'good_step1':
    st.title("📖 教科書販売のご案内")
    st.info("2026年前期の教科書販売は終了しました。現在は次学期の予約受付準備中です。")
    
    st.subheader("🛒 ご購入までの3ステップ")
    st.markdown("""
        <div class="step-container"><span class="step-number">STEP 1</span> 下記ボタンより来店予約を行う</div>
        <div class="step-container"><span class="step-number">STEP 2</span> 予約完了後に発行される「予約番号」を控える</div>
        <div class="step-container"><span class="step-number">STEP 3</span> 予約日時に会場へお越しください</div>
    """, unsafe_allow_html=True)

    st.write("")
    if st.button("次へ：来店予約フォームへ進む", type="primary", use_container_width=True):
        st.session_state.page = 'good_step2'
        st.rerun()

# --- 改善版：予約フォーム ---
elif st.session_state.page == 'good_step2':
    st.title("📝 予約情報入力")
    st.write("以下の項目をご入力ください。")
    
    name = st.text_input("お名前", placeholder="例：山田 太郎")
    tel = st.text_input("電話番号（半角数字のみ）", placeholder="例：09012345678")
    
    # 「教科書の種類」のセレクトボックス項目は削除しました
    
    st.write("---")
    agree = st.checkbox("利用規約に同意する")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("前の画面に戻る", use_container_width=True):
            st.session_state.rsv_num = None
            st.session_state.page = 'good_step1'
            st.rerun()
            
    with col2:
        # 名前、電話番号、規約同意が揃うまでボタンを無効化
        submit_disabled = not (name and tel and agree)
        
        # 予約番号がまだ発行されていない場合のみ「予約を確定する」ボタンを表示
        if st.session_state.rsv_num is None:
            if st.button("予約を確定する", type="primary", use_container_width=True, disabled=submit_disabled):
                random_digits = random.randint(100000, 999999)
                st.session_state.rsv_num = f"RSV-{random_digits}"
                st.rerun()

    # 予約番号が生成された後の表示処理
    if st.session_state.rsv_num:
        st.success("予約が完了しました！予約番号をお控えの上、次のステップへお進みください。")
        st.markdown(f'<div class="rsv-number">予約番号：{st.session_state.rsv_num}</div>', unsafe_allow_html=True)
        st.balloons()
        
        st.write("---")
        # 予約番号の下に新しく「教科書予約に進む」ボタンを追加
        if st.button("👉 教科書予約に進む", type="primary", use_container_width=True):
            st.info("次の教科書選択ページ（または外部の購入サイト）へ遷移する処理をここに記述します。")
