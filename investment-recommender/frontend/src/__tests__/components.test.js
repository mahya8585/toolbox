import { describe, it, expect } from 'vitest'
import { mount } from '@vue/test-utils'
import ProductList from '../components/ProductList.vue'
import SimilarCustomers from '../components/SimilarCustomers.vue'
import MarketTrends from '../components/MarketTrends.vue'

const sampleRecommendations = [
  {
    product: {
      id: 'P001',
      name: 'グローバル株式ファンド',
      type: '投資信託',
      expectedReturn: 7.2,
      riskLevel: '中',
      description: 'テスト説明',
      category: '株式',
      currency: 'JPY',
    },
    score: 0.93,
    reasons: ['類似顧客が購入', '市場トレンド一致'],
    scenarioType: 'SIMILAR_CUSTOMER',
    aiExplanation: 'AI説明テキスト',
  },
]

const sampleCustomers = [
  {
    id: 'S001',
    name: 'A・Kさん (35歳)',
    age: 35,
    similarity: 0.92,
    investmentStyle: '成長重視',
    recentPurchases: [
      { id: 'P001', name: 'グローバル株式ファンド' },
    ],
  },
]

const sampleTrends = [
  {
    id: 'T001',
    name: '金利上昇トレンド',
    direction: 'UP',
    summary: 'テスト要約',
    impact: 'テスト影響',
    category: '債券',
    changePercent: 0.25,
    lastUpdated: '2026-05-28',
  },
]

describe('ProductList', () => {
  it('renders recommendation cards', () => {
    const wrapper = mount(ProductList, {
      props: { recommendations: sampleRecommendations, loading: false, error: false },
    })
    expect(wrapper.text()).toContain('グローバル株式ファンド')
    expect(wrapper.text()).toContain('93')
  })

  it('shows loading skeletons when loading', () => {
    const wrapper = mount(ProductList, {
      props: { recommendations: [], loading: true, error: false },
    })
    expect(wrapper.findAll('.skeleton').length).toBeGreaterThan(0)
  })

  it('shows error message on error', () => {
    const wrapper = mount(ProductList, {
      props: { recommendations: [], loading: false, error: true },
    })
    expect(wrapper.find('.error-box').exists()).toBe(true)
  })
})

describe('SimilarCustomers', () => {
  it('renders customer cards', () => {
    const wrapper = mount(SimilarCustomers, {
      props: { customers: sampleCustomers, loading: false, error: false },
    })
    expect(wrapper.text()).toContain('A・Kさん')
    expect(wrapper.text()).toContain('92')
  })
})

describe('MarketTrends', () => {
  it('renders trend cards', () => {
    const wrapper = mount(MarketTrends, {
      props: { trends: sampleTrends, loading: false, error: false },
    })
    expect(wrapper.text()).toContain('金利上昇トレンド')
  })
})
