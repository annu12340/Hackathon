import { mutation, query } from './_generated/server';
import { v } from 'convex/values';
import { internal } from './_generated/api';
import { Auth } from 'convex/server';

export const getUserId = async (ctx: { auth: Auth }) => {
  return (await ctx.auth.getUserIdentity())?.subject;
};

// Get all culprits for a specific user
export const getCulprits = query({
  args: {},
  handler: async (ctx) => {
    const userId = await getUserId(ctx);
    if (!userId) return null;

    const culprits = await ctx.db
      .query('culprits')
      .filter((q) => q.eq(q.field('userId'), userId))
      .collect();

    return culprits;
  },
});

// Get culprit for a specific culprit
export const getCulprit = query({
  args: {
    id: v.optional(v.id('culprits')),
  },
  handler: async (ctx, args) => {
    const { id } = args;
    if (!id) return null;
    const culprit = await ctx.db.get(id);
    return culprit;
  },
});

// Create a new culprit for a user
export const createCulprit = mutation({
  args: {
    title: v.string(),
    content: v.string(),
    isSummary: v.boolean(),
  },
  handler: async (ctx, { title, content, isSummary }) => {
    const userId = await getUserId(ctx);
    if (!userId) throw new Error('User not found');
    const culpritId = await ctx.db.insert('culprits', { userId, title, content });

    // if (isSummary) {
    //   await ctx.scheduler.runAfter(0, internal.openai.summary, {
    //     id: culpritId,
    //     title,
    //     content,
    //   });
    // }

    return culpritId;
  },
});

export const deleteCulprit = mutation({
  args: {
    culpritId: v.id('culprits'),
  },
  handler: async (ctx, args) => {
    await ctx.db.delete(args.culpritId);
  },
});
