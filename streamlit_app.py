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
    
    /* 入力フォームの視認性向上（改善された枠線） */
    .stTextInput input, .stSelectbox div {
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
    
    /* 検索画面（3枚目）用の補足テキストスタイル */
    .search-hint {
        font-size: 0.85rem;
        color: #495057;
        margin-bottom: 5px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ページ遷移と状態の管理 ---
if 'page' not in st.session_state:
    st.session_state.page = 'good_step1'
if 'rsv_num' not in st.session_state:
    st.session_state.rsv_num = None

# =================================================================
# 1枚目：ご利用の流れ
# =================================================================
if st.session_state.page == 'good_step1':
    st.title("📖 教科書販売のご案内")
    st.info("2026年前期の教科書販売は終了しました。現在は次学期の予約受付準備中です。")
    
    st.subheader("🛒 ご購入までの3ステップ")
    st.markdown("""
        <div class="step-container"><span class="step-number">STEP 1</span> 下記ボタンより来店予約を行う</div>
        <div class="step-container"><span class="step-number">STEP 2</span> 予約完了後に発行される「予約番号」を控える</div>
        <div class="step-container"><span class="step-number">STEP 3</span> 教科書を検索・予約して当日会場へ行く</div>
    """, unsafe_allow_html=True)

    st.write("")
    if st.button("次へ：来店予約フォームへ進む", type="primary", use_container_width=True):
        st.session_state.page = 'good_step2'
        st.rerun()

# =================================================================
# 2枚目：予約フォーム＆予約番号発行
# =================================================================
elif st.session_state.page == 'good_step2':
    st.title("📝 予約情報入力")
    st.write("以下の項目をご入力ください。")
    
    name = st.text_input("お名前", placeholder="例：山田 太郎")
    tel = st.text_input("電話番号（半角数字のみ）", placeholder="例：09012345678")
    
    st.write("---")
    agree = st.checkbox("利用規約に同意する")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("前の画面に戻る", use_container_width=True):
            st.session_state.rsv_num = None
            st.session_state.page = 'good_step1'
            st.rerun()
            
    with col2:
        submit_disabled = not (name and tel and agree)
        
        # 予約確定ボタン（未発行の時だけ表示）
        if st.session_state.rsv_num is None:
            if st.button("予約を確定する", type="primary", use_container_width=True, disabled=submit_disabled):
                random_digits = random.randint(100000, 999999)
                st.session_state.rsv_num = f"RSV-{random_digits}"
                st.rerun()

    # 予約が確定した後の表示
    if st.session_state.rsv_num:
        st.success("予約が完了しました！予約番号をお控えの上、次のステップへお進みください。")
        st.markdown(f'<div class="rsv-number">予約番号：{st.session_state.rsv_num}</div>', unsafe_allow_html=True)
        st.balloons()
        
        st.write("---")
        # 予約完了後に現れる遷移ボタン
        if st.button("👉 教科書予約に進む", type="primary", use_container_width=True):
            st.session_state.page = 'good_step3'
            st.rerun()

# =================================================================
# 3枚目：追加された教科書検索・予約画面
# =================================================================
elif st.session_state.page == 'good_step3':
    st.title("🔍 教科書 検索・予約")
    st.write("購入する教科書を検索してください。")
    
    # 予約番号の引き継ぎ表示（ユーザーが迷わないための親切設計）
    st.info(f"現在の来店予約番号: {st.session_state.rsv_num}")
    
    # 画像にあった「学部・学年」の入力欄
    st.markdown('<p class="search-hint">・学部（学部名の頭一文字を入力してください。文・教・法・理・医・薬・工もしくは大学院・その他）</p>', unsafe_allow_html=True)
    col_fac, col_grade = st.columns([3, 1])
    with col_fac:
        st.text_input("学部入力", label_visibility="collapsed", placeholder="例：工")
    with col_grade:
        st.selectbox("学年", ["選択しない", "1年", "2年", "3年", "4年"], label_visibility="collapsed")
        
    # 教員名で検索
    st.markdown('<p class="search-hint">・教員名で検索</p>', unsafe_allow_html=True)
    st.text_input("教員名", label_visibility="collapsed", placeholder="例：山田")
    
    # 書名or商品名で検索
    st.markdown('<p class="search-hint">・書名or商品名で検索</p>', unsafe_allow_html=True)
    st.text_input("書名", label_visibility="collapsed", placeholder="例：微分積分学")
    
    # 講義名（科目名）で検索
    st.markdown('<p class="search-hint">・講義名（科目名）で検索</p>', unsafe_allow_html=True)
    st.text_input("講義名", label_visibility="collapsed", placeholder="例：基礎数学")
    
    # 区分２（教科書・参考書）
    st.markdown('<p class="search-hint">・区分２（教科書・参考書）</p>', unsafe_allow_html=True)
    st.text_input("区分２", label_visibility="collapsed", placeholder="例：教科書")
    
    st.write("---")
    
    # 画像のような大きな緑色の「検索する」ボタン
    if st.button("🔍 検索する ➔", type="secondary", use_container_width=True):
        st.success("検索結果を表示します...（※実際のシステムではここに該当の教科書が一覧表示されます）")
        
    if st.button("⬅ 予約フォームに戻る"):
        st.session_state.page = 'good_step2'
        st.rerun()
