<template>
  <section class="section">
    <div class="section-header">
      <h2 class="section-title">
        <span class="icon">👥</span> 類似顧客の投資行動
      </h2>
      <p class="section-sub">あなたに似たお客さまが選んだ商品をご紹介します 💌</p>
    </div>

    <div v-if="loading" class="grid">
      <div v-for="i in 3" :key="i" class="skeleton" style="height:160px" />
    </div>

    <div v-else-if="error" class="error-box">
      😢 データを取得できませんでした。
    </div>

    <div v-else class="grid">
      <div v-for="customer in customers" :key="customer.id" class="customer-card">
        <!-- Avatar + basic info -->
        <div class="customer-header">
          <div class="avatar">{{ initials(customer.name) }}</div>
          <div>
            <p class="customer-name">{{ customer.name }}</p>
            <p class="customer-age">{{ customer.age }}歳 · {{ customer.investmentStyle }}</p>
          </div>
          <div class="similarity-badge">
            <span class="similarity-num">{{ Math.round(customer.similarity * 100) }}</span>
            <span class="similarity-unit">%一致</span>
          </div>
        </div>

        <!-- Similarity bar -->
        <div class="sim-bar-wrap">
          <div class="sim-bar" :style="{ width: (customer.similarity * 100) + '%' }" />
        </div>

        <!-- Recent purchases -->
        <p class="purchases-label">📦 最近の購入商品</p>
        <div class="purchases">
          <span
            v-for="p in customer.recentPurchases"
            :key="p.id"
            class="purchase-chip"
          >{{ p.name }}</span>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
defineProps({
  customers: { type: Array, default: () => [] },
  loading:   { type: Boolean, default: false },
  error:     { type: Boolean, default: false },
})

// Generate 2-char initials from "山田 太郎" → "山田"
const initials = (name) => name ? name.slice(0, 2) : '??'
</script>

<style scoped>
.section { margin-bottom: 2rem; }
.section-header { margin-bottom: 1.25rem; }
.section-title  { font-size: 1.4rem; font-weight: 700; color: #0284c7; display: flex; align-items: center; gap: 8px; }
.section-sub    { font-size: 0.9rem; color: #7dd3fc; margin-top: 4px; }

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 1rem;
}

.customer-card {
  background: linear-gradient(135deg, #f0f9ff 0%, #faf5ff 100%);
  border-radius: var(--radius-lg);
  padding: 1.25rem;
  box-shadow: var(--shadow-sm);
  border: 1.5px solid var(--sky);
  transition: transform 0.2s, box-shadow 0.2s;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}
.customer-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 24px rgba(56, 189, 248, 0.2);
}

/* Header */
.customer-header {
  display: flex;
  align-items: center;
  gap: 10px;
}
.avatar {
  width: 42px; height: 42px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--sky), var(--lavender));
  display: flex; align-items: center; justify-content: center;
  font-size: 0.85rem; font-weight: 700; color: #1e40af;
  flex-shrink: 0;
}
.customer-name { font-weight: 700; font-size: 0.92rem; color: var(--gray-800); }
.customer-age  { font-size: 0.75rem; color: var(--gray-600); margin-top: 1px; }

.similarity-badge {
  margin-left: auto;
  background: var(--sky);
  border-radius: var(--radius-sm);
  padding: 4px 8px;
  text-align: center;
  line-height: 1;
}
.similarity-num  { font-size: 1.1rem; font-weight: 700; color: #0284c7; }
.similarity-unit { font-size: 0.68rem; color: #0369a1; display: block; }

/* Similarity bar */
.sim-bar-wrap {
  height: 6px;
  background: var(--gray-100);
  border-radius: 999px;
  overflow: hidden;
}
.sim-bar {
  height: 100%;
  background: linear-gradient(90deg, var(--sky-dark), var(--lavender-dark));
  border-radius: 999px;
  transition: width 0.8s ease;
}

/* Purchases */
.purchases-label { font-size: 0.78rem; font-weight: 600; color: var(--gray-600); }
.purchases { display: flex; flex-wrap: wrap; gap: 6px; }
.purchase-chip {
  background: var(--white);
  border: 1.5px solid var(--pink-200);
  border-radius: 999px;
  padding: 3px 10px;
  font-size: 0.75rem;
  color: var(--pink-500);
  font-weight: 500;
  white-space: nowrap;
}

.error-box {
  padding: 1rem; background: #fff1f2;
  border-radius: var(--radius-md); color: #be123c;
  font-size: 0.9rem; border: 1.5px solid #fecdd3;
}
</style>
