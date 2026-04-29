import streamlit as st

# --- ページ設定（親しみやすいタイトルに） ---
st.set_page_config(page_title="教科書販売 公式サイト", layout="centered")

# --- 改善されたスタイル設定 ---
st.markdown("""
    <style>
    /* 明確な「ステップ表示」のデザイン（ボタンと混同させない） */
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
    </style>
    """, unsafe_allow_html=True)

# --- ページ遷移の管理 ---
if 'page' not in st.session_state:
    st.session_state.page = 'good_step1'

# --- 改善版：ご利用の流れ ---
if st.session_state.page == 'good_step1':
    st.title("📖 教科書販売のご案内")
    
    # お知らせ：重要な情報は目立つが威圧的でない形式で
    st.info("2026年前期の教科書販売は終了しました。現在は次学期の予約受付準備中です。")
    
    st.subheader("🛒 ご購入までの3ステップ")
    
    # 改善：ボタンではなく「流れ」であることを明示
    st.markdown("""
        <div class="step-container"><span class="step-number">STEP 1</span> 下記ボタンより来店予約を行う</div>
        <div class="step-container"><span class="step-number">STEP 2</span> 予約完了後に発行される「注文番号」を控える</div>
        <div class="step-container"><span class="step-number">STEP 3</span> 予約日時に会場へお越しください</div>
    """, unsafe_allow_html=True)

    st.write("")
    
    # 改善：一番重要なアクションを、一番目立つ「大きなボタン」に変更
    if st.button("次へ：来店予約フォームへ進む", type="primary", use_container_width=True):
        st.session_state.page = 'good_step2'
        st.rerun()

# --- 改善版：予約フォーム ---
elif st.session_state.page == 'good_step2':
    st.title("📝 予約情報入力")
    st.write("以下の項目をご入力ください。")
    
    # 改善：ラベルを明確にし、入力例（ヘルプ）を配置
    name = st.text_input("お名前", placeholder="例：山田 太郎")
    tel = st.text_input("電話番号（半角数字のみ）", placeholder="例：09012345678")
    
    category = st.selectbox(
        "教科書の種類を選択してください", 
        ["選択してください", "文系一般", "理系専門", "医学系", "語学", "その他"],
        index=0
    )
    
    st.write("---")
    
    # 改善：規約は送信ボタンの直前に配置し、納得感を高める
    agree = st.checkbox("利用規約に同意する")

    # 改善：送信ボタンは中央または左側に大きく。
    # 完了時は明確な成功メッセージを表示。
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("前の画面に戻る", use_container_width=True):
            st.session_state.page = 'good_step1'
            st.rerun()
    with col2:
        # 入力チェックをしてから送信可能にする（これも良いUI）
        submit_disabled = not (name and tel and category != "選択してください" and agree)
        if st.button("予約を確定する", type="primary", use_container_width=True, disabled=submit_disabled):
            st.success("予約が完了しました！注文番号：TX-2026 をお控えください。")
            st.balloons()
