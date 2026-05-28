<template>
  <section class="section">
    <div class="section-header">
      <h2 class="section-title">
        <span class="icon">🌍</span> 市場トレンド
      </h2>
      <p class="section-sub">最新の市場動向をAIがまとめました 📰</p>
    </div>

    <div v-if="loading" class="grid">
      <div v-for="i in 4" :key="i" class="skeleton" style="height:140px" />
    </div>

    <div v-else-if="error" class="error-box">
      😢 トレンド情報を取得できませんでした。
    </div>

    <div v-else class="grid">
      <div
        v-for="trend in trends"
        :key="trend.id"
        class="trend-card"
        :class="trendColorClass(trend.direction)"
      >
        <div class="trend-top">
          <span class="trend-icon">{{ trendIcon(trend.direction) }}</span>
          <span class="trend-name">{{ trend.name }}</span>
          <span class="trend-change" :class="changeClass(trend.direction)">
            {{ trend.changePercent > 0 ? '+' : '' }}{{ trend.changePercent }}%
          </span>
        </div>

        <span class="badge" :class="categoryBadge(trend.category)">{{ trend.category }}</span>

        <p class="trend-summary">{{ trend.summary }}</p>

        <div class="trend-impact">
          <span class="impact-icon">💡</span>
          <span>{{ trend.impact }}</span>
        </div>

        <p class="trend-date">{{ trend.lastUpdated }} 更新</p>
      </div>
    </div>
  </section>
</template>

<script setup>
defineProps({
  trends:  { type: Array, default: () => [] },
  loading: { type: Boolean, default: false },
  error:   { type: Boolean, default: false },
})

const trendIcon = (dir) => ({ UP: '📈', DOWN: '📉', STABLE: '➡️' }[dir] ?? '📊')

const trendColorClass = (dir) => ({
  UP:     'trend-up',
  DOWN:   'trend-down',
  STABLE: 'trend-stable',
}[dir] ?? '')

const changeClass = (dir) => ({
  UP:     'change-up',
  DOWN:   'change-down',
  STABLE: 'change-stable',
}[dir] ?? '')

const categoryBadge = (cat) => ({
  '株式':   'badge-pink',
  '債券':   'badge-sky',
  '不動産': 'badge-mint',
  '新興国': 'badge-peach',
}[cat] ?? 'badge-lavender')
</script>

<style scoped>
.section { margin-bottom: 2rem; }
.section-header { margin-bottom: 1.25rem; }
.section-title  { font-size: 1.4rem; font-weight: 700; color: #059669; display: flex; align-items: center; gap: 8px; }
.section-sub    { font-size: 0.9rem; color: #6ee7b7; margin-top: 4px; }

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  gap: 1rem;
}

.trend-card {
  border-radius: var(--radius-lg);
  padding: 1.1rem 1.25rem;
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
  border: 1.5px solid transparent;
  transition: transform 0.2s, box-shadow 0.2s;
  background: #fff;
}
.trend-card:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-lg);
}

.trend-up     { border-color: #bbf7d0; background: linear-gradient(135deg, #f0fdf4 0%, #fdf4ff 100%); }
.trend-down   { border-color: #fecdd3; background: linear-gradient(135deg, #fff1f2 0%, #fffbeb 100%); }
.trend-stable { border-color: var(--sky);  background: linear-gradient(135deg, #f0f9ff 0%, #f5f3ff 100%); }

.trend-top {
  display: flex;
  align-items: center;
  gap: 8px;
}
.trend-icon  { font-size: 1.4rem; }
.trend-name  { font-weight: 700; font-size: 0.92rem; color: var(--gray-800); flex: 1; }
.trend-change { font-size: 0.88rem; font-weight: 700; white-space: nowrap; }
.change-up     { color: #059669; }
.change-down   { color: #be123c; }
.change-stable { color: #0284c7; }

.trend-summary {
  font-size: 0.82rem;
  color: var(--gray-700);
  line-height: 1.55;
}

.trend-impact {
  display: flex;
  gap: 6px;
  font-size: 0.8rem;
  color: var(--gray-600);
  background: var(--yellow);
  border-radius: var(--radius-sm);
  padding: 6px 10px;
  line-height: 1.45;
}
.impact-icon { flex-shrink: 0; }

.trend-date { font-size: 0.7rem; color: #9ca3af; text-align: right; margin-top: auto; }

.error-box {
  padding: 1rem; background: #fff1f2;
  border-radius: var(--radius-md); color: #be123c;
  font-size: 0.9rem; border: 1.5px solid #fecdd3;
}
</style>
