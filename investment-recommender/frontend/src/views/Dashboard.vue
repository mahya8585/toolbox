<template>
  <div class="page">
    <!-- ── Header ───────────────────────────────────────── -->
    <header class="header">
      <div class="header-inner">
        <div class="logo">
          <span class="logo-icon">💎</span>
          <span class="logo-text">AI投資レコメンド</span>
        </div>

        <!-- Customer selector -->
        <div class="customer-selector">
          <label class="selector-label">顧客を選択</label>
          <select v-model="selectedCustomerId" class="selector" @change="loadAll">
            <option v-for="c in CUSTOMER_LIST" :key="c.id" :value="c.id">
              {{ c.label }}
            </option>
          </select>
        </div>
      </div>
    </header>

    <!-- ── Customer profile banner ──────────────────────── -->
    <transition name="fade">
      <div v-if="customer" class="profile-banner">
        <div class="profile-avatar">{{ customer.name.slice(0, 2) }}</div>
        <div class="profile-info">
          <p class="profile-name">{{ customer.name }} <span class="profile-age">{{ customer.age }}歳</span></p>
          <div class="profile-tags">
            <span class="badge badge-lavender">{{ customer.investmentGoal }}</span>
            <span class="badge" :class="riskBadge(customer.riskTolerance)">
              リスク許容度: {{ customer.riskTolerance }}
            </span>
            <span class="badge badge-sky">{{ customer.preferredCategory }}好み</span>
          </div>
        </div>
        <div class="profile-message">
          <p>🌸 {{ customer.name }}さん、今日のおすすめをご確認ください！</p>
        </div>
      </div>
    </transition>

    <!-- ── Main content ──────────────────────────────────── -->
    <main class="main">
      <!-- Section 1: Recommendations -->
      <ProductList
        :recommendations="recommendations"
        :loading="loadingRecs"
        :error="!!errorRecs"
      />

      <!-- Section 2 + 3 side by side on large screens -->
      <div class="two-col">
        <SimilarCustomers
          :customers="similarCustomers"
          :loading="loadingSimilar"
          :error="!!errorSimilar"
        />
        <MarketTrends
          :trends="marketTrends"
          :loading="loadingTrends"
          :error="!!errorTrends"
        />
      </div>
    </main>

    <!-- ── Footer ───────────────────────────────────────── -->
    <footer class="footer">
      <p>💕 Investment Recommender · ローカル検証モード (ダミーデータ)</p>
    </footer>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '../services/api.js'
import ProductList from '../components/ProductList.vue'
import SimilarCustomers from '../components/SimilarCustomers.vue'
import MarketTrends from '../components/MarketTrends.vue'

const CUSTOMER_LIST = [
  { id: 'C001', label: '田中 花子（35歳・中リスク）' },
  { id: 'C002', label: '山田 太郎（52歳・低リスク）' },
  { id: 'C003', label: '鈴木 美咲（28歳・高リスク）' },
  { id: 'C004', label: '佐藤 健一（45歳・中リスク）' },
]

const selectedCustomerId = ref('C001')
const customer = ref(null)

const recommendations   = ref([])
const loadingRecs       = ref(false)
const errorRecs         = ref(null)

const similarCustomers  = ref([])
const loadingSimilar    = ref(false)
const errorSimilar      = ref(null)

const marketTrends      = ref([])
const loadingTrends     = ref(false)
const errorTrends       = ref(null)

async function loadAll() {
  const id = selectedCustomerId.value
  await Promise.all([loadRecommendations(id), loadSimilar(id), loadTrends()])
}

async function loadRecommendations(id) {
  loadingRecs.value = true
  errorRecs.value   = null
  try {
    const data = await api.getRecommendations(id)
    customer.value        = data.customer
    recommendations.value = data.recommendations
  } catch (e) {
    errorRecs.value = e
  } finally {
    loadingRecs.value = false
  }
}

async function loadSimilar(id) {
  loadingSimilar.value = true
  errorSimilar.value   = null
  try {
    similarCustomers.value = await api.getSimilarCustomers(id)
  } catch (e) {
    errorSimilar.value = e
  } finally {
    loadingSimilar.value = false
  }
}

async function loadTrends() {
  loadingTrends.value = true
  errorTrends.value   = null
  try {
    marketTrends.value = await api.getMarketTrends()
  } catch (e) {
    errorTrends.value = e
  } finally {
    loadingTrends.value = false
  }
}

const riskBadge = (level) => ({
  '低': 'badge-mint',
  '中': 'badge-yellow',
  '高': 'badge-peach',
}[level] ?? 'badge-sky')

onMounted(loadAll)
</script>

<style scoped>
/* ── Layout ──────────────────────────────────────────── */
.page { min-height: 100vh; display: flex; flex-direction: column; }

/* ── Header ──────────────────────────────────────────── */
.header {
  background: linear-gradient(135deg, #fdf2f8 0%, #faf5ff 100%);
  border-bottom: 2px solid var(--pink-100);
  position: sticky;
  top: 0;
  z-index: 100;
  box-shadow: 0 2px 12px rgba(236, 72, 153, 0.08);
}
.header-inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 1rem 1.5rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
}
.logo { display: flex; align-items: center; gap: 10px; }
.logo-icon { font-size: 1.8rem; }
.logo-text {
  font-family: 'Poppins', sans-serif;
  font-size: 1.3rem;
  font-weight: 700;
  background: linear-gradient(135deg, var(--pink-500), #7c3aed);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

/* Customer selector */
.customer-selector { display: flex; align-items: center; gap: 8px; }
.selector-label { font-size: 0.82rem; color: var(--gray-600); font-weight: 600; white-space: nowrap; }
.selector {
  background: white;
  border: 2px solid var(--pink-200);
  border-radius: var(--radius-sm);
  padding: 6px 12px;
  font-size: 0.85rem;
  color: var(--gray-700);
  cursor: pointer;
  outline: none;
  transition: border-color 0.2s;
}
.selector:focus { border-color: var(--pink-400); }

/* ── Profile banner ──────────────────────────────────── */
.profile-banner {
  max-width: 1200px;
  margin: 1.5rem auto 0;
  padding: 0 1.5rem;
  display: flex;
  align-items: center;
  gap: 1rem;
  background: linear-gradient(135deg, #fff0f6, #fdf4ff, #f0f9ff);
  border-radius: var(--radius-lg);
  padding: 1rem 1.5rem;
  border: 2px solid var(--pink-100);
  box-shadow: var(--shadow-sm);
  flex-wrap: wrap;
}
.profile-avatar {
  width: 52px; height: 52px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--pink-400), var(--lavender-dark));
  display: flex; align-items: center; justify-content: center;
  font-size: 1.1rem; font-weight: 700; color: white;
  flex-shrink: 0;
  box-shadow: 0 4px 12px rgba(236, 72, 153, 0.3);
}
.profile-name  { font-weight: 700; font-size: 1rem; color: var(--gray-800); }
.profile-age   { font-size: 0.82rem; color: var(--gray-600); font-weight: 400; margin-left: 6px; }
.profile-tags  { display: flex; gap: 6px; flex-wrap: wrap; margin-top: 6px; }
.profile-message {
  margin-left: auto;
  font-size: 0.88rem;
  color: var(--pink-500);
  font-weight: 600;
  background: var(--pink-50);
  padding: 6px 12px;
  border-radius: var(--radius-sm);
  border: 1px solid var(--pink-100);
}

/* ── Main ────────────────────────────────────────────── */
.main {
  flex: 1;
  max-width: 1200px;
  margin: 0 auto;
  padding: 1.5rem;
  width: 100%;
}

.two-col {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
}
@media (max-width: 768px) {
  .two-col { grid-template-columns: 1fr; }
}

/* ── Footer ──────────────────────────────────────────── */
.footer {
  text-align: center;
  padding: 1rem;
  font-size: 0.78rem;
  color: #d1d5db;
  border-top: 1px solid var(--gray-100);
  margin-top: auto;
}

/* Fade transition (from global.css) */
.fade-enter-active, .fade-leave-active { transition: opacity 0.4s ease; }
.fade-enter-from, .fade-leave-to { opacity: 0; }
</style>
