<template>
  <section class="section">
    <div class="section-header">
      <h2 class="section-title">
        <span class="icon">💎</span> おすすめ投資商品
      </h2>
      <p class="section-sub">あなたに最適な商品をAIが分析しました ✨</p>
    </div>

    <!-- Loading skeleton -->
    <div v-if="loading" class="grid">
      <div v-for="i in 3" :key="i" class="skeleton" style="height:220px" />
    </div>

    <!-- Error -->
    <div v-else-if="error" class="error-box">
      <span>😢 データを取得できませんでした。バックエンドが起動しているか確認してください。</span>
    </div>

    <!-- Cards -->
    <div v-else class="grid">
      <transition-group name="pop" appear>
        <div
          v-for="(rec, idx) in recommendations"
          :key="rec.product.id"
          class="rec-card"
          :class="{ 'top-pick': idx === 0 }"
        >
          <!-- Rank badge -->
          <div class="rank-badge" :class="rankClass(idx)">
            {{ rankLabel(idx) }}
          </div>

          <!-- Score bar -->
          <div class="score-row">
            <span class="score-label">AIスコア</span>
            <div class="score-bar-wrap">
              <div class="score-bar" :style="{ width: (rec.score * 100) + '%' }" />
            </div>
            <span class="score-num">{{ Math.round(rec.score * 100) }}</span>
          </div>

          <!-- Product info -->
          <div class="product-info">
            <div class="product-header">
              <span class="product-icon">{{ productIcon(rec.product.type) }}</span>
              <div>
                <p class="product-name">{{ rec.product.name }}</p>
                <div class="product-tags">
                  <span class="badge badge-lavender">{{ rec.product.type }}</span>
                  <span class="badge" :class="riskBadgeClass(rec.product.riskLevel)">
                    リスク{{ rec.product.riskLevel }}
                  </span>
                </div>
              </div>
            </div>
            <p class="product-desc">{{ rec.product.description }}</p>
          </div>

          <!-- Return -->
          <div class="return-row">
            <span class="return-label">期待リターン</span>
            <span class="return-value">+{{ rec.product.expectedReturn }}%</span>
          </div>

          <!-- Reasons -->
          <div class="reasons">
            <p class="reasons-title">📌 推薦理由</p>
            <ul>
              <li v-for="(reason, ri) in rec.reasons" :key="ri">
                <span class="reason-dot">✦</span>{{ reason }}
              </li>
            </ul>
          </div>

          <!-- AI explanation -->
          <details class="ai-explanation">
            <summary>🤖 AIの詳しい説明を見る</summary>
            <p>{{ rec.aiExplanation }}</p>
          </details>
        </div>
      </transition-group>
    </div>
  </section>
</template>

<script setup>
const props = defineProps({
  recommendations: { type: Array, default: () => [] },
  loading: { type: Boolean, default: false },
  error: { type: Boolean, default: false },
})

const RANK_LABELS = ['🥇 第1位', '🥈 第2位', '🥉 第3位']
const rankLabel = (idx) => RANK_LABELS[idx] ?? `#${idx + 1}`
const rankClass = (idx) => ['rank-gold', 'rank-silver', 'rank-bronze'][idx] ?? 'rank-other'

const PRODUCT_ICONS = {
  '投資信託': '📊', 'ETF': '📈', 'REIT': '🏢', '株式': '💹', '債券': '📋',
}
const productIcon = (type) => PRODUCT_ICONS[type] ?? '💼'

const riskBadgeClass = (level) => ({
  '低': 'badge-mint',
  '中': 'badge-yellow',
  '高': 'badge-peach',
}[level] ?? 'badge-sky')
</script>

<style scoped>
.section { margin-bottom: 2rem; }

.section-header { margin-bottom: 1.25rem; }
.section-title  { font-size: 1.4rem; font-weight: 700; color: #7c3aed; display: flex; align-items: center; gap: 8px; }
.section-sub    { font-size: 0.9rem; color: #a78bfa; margin-top: 4px; }

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1.25rem;
}

.rec-card {
  background: #fff;
  border-radius: var(--radius-lg);
  padding: 1.25rem;
  box-shadow: var(--shadow-md);
  border: 2px solid transparent;
  transition: transform 0.2s, box-shadow 0.2s, border-color 0.2s;
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}
.rec-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg);
  border-color: var(--pink-200);
}
.top-pick {
  border-color: var(--pink-400);
  background: linear-gradient(135deg, #fff0f6 0%, #fdf4ff 100%);
}

/* Rank badge */
.rank-badge {
  position: absolute;
  top: -10px; right: 14px;
  font-size: 0.75rem;
  font-weight: 700;
  padding: 3px 12px;
  border-radius: 999px;
  letter-spacing: 0.03em;
}
.rank-gold   { background: #fef9c3; color: #b45309; border: 1.5px solid #facc15; }
.rank-silver { background: #f3f4f6; color: #4b5563; border: 1.5px solid #d1d5db; }
.rank-bronze { background: var(--peach); color: #9a3412; border: 1.5px solid #fb923c; }

/* Score bar */
.score-row {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-top: 12px;
}
.score-label { font-size: 0.72rem; color: #9ca3af; white-space: nowrap; }
.score-bar-wrap {
  flex: 1;
  height: 8px;
  background: var(--gray-100);
  border-radius: 999px;
  overflow: hidden;
}
.score-bar {
  height: 100%;
  background: linear-gradient(90deg, var(--pink-400), var(--lavender-dark));
  border-radius: 999px;
  transition: width 0.8s ease;
}
.score-num { font-size: 0.82rem; font-weight: 700; color: var(--pink-500); min-width: 28px; text-align: right; }

/* Product info */
.product-header {
  display: flex;
  gap: 10px;
  align-items: flex-start;
}
.product-icon { font-size: 2rem; line-height: 1; }
.product-name { font-size: 1rem; font-weight: 700; color: var(--gray-800); line-height: 1.3; }
.product-tags { display: flex; gap: 4px; flex-wrap: wrap; margin-top: 4px; }
.product-desc { font-size: 0.82rem; color: var(--gray-600); line-height: 1.5; }

/* Return */
.return-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: var(--mint);
  border-radius: var(--radius-sm);
  padding: 6px 12px;
}
.return-label { font-size: 0.78rem; color: #065f46; }
.return-value { font-size: 1rem; font-weight: 700; color: #059669; }

/* Reasons */
.reasons-title { font-size: 0.8rem; font-weight: 700; color: var(--gray-700); margin-bottom: 4px; }
.reasons ul { list-style: none; display: flex; flex-direction: column; gap: 3px; }
.reasons li { font-size: 0.8rem; color: var(--gray-600); display: flex; gap: 6px; align-items: baseline; }
.reason-dot { color: var(--pink-400); font-size: 0.6rem; flex-shrink: 0; }

/* AI explanation */
.ai-explanation {
  margin-top: auto;
  font-size: 0.8rem;
}
.ai-explanation summary {
  cursor: pointer;
  color: #7c3aed;
  font-weight: 600;
  user-select: none;
  padding: 4px 0;
}
.ai-explanation p {
  margin-top: 6px;
  padding: 10px;
  background: #fdf4ff;
  border-radius: var(--radius-sm);
  border-left: 3px solid var(--lavender-dark);
  color: var(--gray-700);
  line-height: 1.6;
}

/* Error */
.error-box {
  padding: 1rem 1.25rem;
  background: #fff1f2;
  border-radius: var(--radius-md);
  color: #be123c;
  font-size: 0.9rem;
  border: 1.5px solid #fecdd3;
}

/* Transition */
.pop-enter-active { animation: pop-in 0.35s ease both; }
@keyframes pop-in {
  0%   { opacity: 0; transform: scale(0.92) translateY(12px); }
  100% { opacity: 1; transform: scale(1) translateY(0); }
}
</style>
